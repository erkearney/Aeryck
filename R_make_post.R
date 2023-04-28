library("argparse")
library("RSQLite")
library("knitr")

parse_args <- function() {
  parser <- ArgumentParser(
    description = "Ingest a markdown file and insert it into the database"
  )

  parser$add_argument(
    "input_file",
    help = "Path to the .Rmd file"
  )

  parser$add_argument(
    "-u", "--update",
    action = "store_true",
    help = "If TRUE, update an existing post instead of creating a new one"
  )

  parser$parse_args()
}


convert_Rmd_to_md <- function(input_file) {

}


create_md_file_and_plots <- function(input_file) {
  md_file <- knit(input_file)
  filename <- basename(md_file)
  move_and_rename_plots(md_file, "/static/images")

  md_file_path <- paste0("posts/", filename)
  file.copy(filename, md_file_path)
  file.remove(filename)

  return(md_file_path)
}


move_and_rename_plots <- function(input_file, image_dir) {
  # The knitr library creates plots from code in the R markdown file, we need to
  # move those plots to comply with the Flask directory structure
  post_title <- tools::file_path_sans_ext(input_file)
  image_post_dir <- paste0(image_dir, "/", post_title)
  if (!dir.exists(paste0("app/", image_post_dir))) {
    dir.create(paste0("app/", image_post_dir), recursive = TRUE)
  }
  re_pattern <- "!\\[(.*)\\]\\(figure/unnamed-chunk-(.*)\\)"
  lines <- readLines(input_file)
  updated_lines <- lines
  figure_number <- 1

  for (i in seq_along(lines)) {
    match <- regexpr(re_pattern, lines[i], perl = TRUE)
    if (attr(match, "match.length") > 0) {
      old_image_line <- regmatches(lines[i], match)
      re_old_image_path <- "\\(figure/.*?\\.png\\)"
      old_image_match <- regexpr(re_old_image_path, old_image_line)
      old_image_path <- regmatches(old_image_line, old_image_match)
      old_image_path <- gsub("[\\(\\)]", "", old_image_path)
      new_image_filename <- paste0(figure_number, ".png")
      new_image_path <- file.path(image_post_dir, new_image_filename)
      file.copy(old_image_path, paste0("app/", new_image_path))
      file.remove(old_image_path)

      newline <- paste0(
        "![", post_title, ": Figure ", figure_number, "]",
        "(", image_post_dir, "/", new_image_filename, ")"
      )
      figure_number <- figure_number + 1
      updated_lines[i] <- newline
    }
  }
  unlink("figure", recursive = TRUE)
  writeLines(updated_lines, input_file)
}


args <- parse_args()
md_file <- create_md_file_and_plots(args$input_file)

if (args$update == TRUE) {
  system(paste("python3 make_post.py", md_file, "-u"))
} else {
  system(paste("python3 make_post.py", md_file))
}
