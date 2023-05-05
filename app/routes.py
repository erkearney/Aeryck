"""
Hook urls to html files in the templates directory.
"""
from typing import Optional, Tuple
from flask import render_template, session, g, Response
from werkzeug.exceptions import HTTPException
import markdown
from app import app, database


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """
    Main landing page of aeryck.com.
    """
    db_conn = database.get_database()

    welcome_post = db_conn.execute(
        'SELECT id, title'
        ' FROM post'
        ' WHERE title = "Welcome"'
    ).fetchone()
    session['post_id'] = welcome_post['id']

    return show_post(welcome_post['title'])


@app.route('/blog')
def blog():
    """
    Displays the titles of blog posts, with links to take the user to each
    post.
    """
    db_conn = database.get_database()
    posts = db_conn.execute(
        'SELECT * FROM post ORDER BY created DESC;'
    ).fetchall()
    return render_template('blog.html', posts=posts, title='Blog')


def get_post_title_by_id(post_id: int) -> Optional[str]:
    """
    Retrieve the post title for a given post ID.

    Query the database to get the post title corresponding to the given post ID.
    If the post ID does not exist, return None.

    Args:
        post_id: The ID of the post to retrieve the title for.

    Returns:
        The post title as a string, or None if the post ID does not exist.

    """
    db_conn = database.get_database()
    post = db_conn.execute(
        "SELECT title"
        " FROM post"
        " WHERE id = ?", (post_id,),
    ).fetchone()

    return post['title'] if post else None


def get_post(post_title):
    """
    Find a post by the posts' title.

    """
    db_conn = database.get_database()
    post = db_conn.execute(
        'SELECT id, title, body, created'
        ' FROM post'
        ' WHERE title = ?', (post_title,),
    ).fetchone()

    return post


@app.route("/post:<string:post_title>", methods=["GET"])
def show_post(post_title: str) -> Response:
    """
    Render a post from the database.

    Retrieve and display a post by its title. The post's ID is used to find
    the older, newer, and newest posts based on their ID values. The post
    content is converted from Markdown to HTML before being rendered.

    Args:
        post_title: The title of the post to display.

    Returns:
        A rendered template with the post content and navigation links.

    """
    db_conn = database.get_database()
    post = get_post(post_title)
    post_id = post["id"]
    g.id = post_id
    title = post['title']

    older_row = db_conn.execute(
        'SELECT MAX(id), title'
        ' FROM post'
        ' WHERE id < ?', (post_id,),
    ).fetchone()
    older_title = older_row["title"]

    newer_row = db_conn.execute(
        'SELECT MIN(id), title'
        ' FROM post'
        ' WHERE id > ?', (post_id,),
    ).fetchone()
    newer_title = newer_row["title"]

    newest_row = db_conn.execute(
        'SELECT MAX(id) AS id, title'
        ' FROM post',
    ).fetchone()
    newest_title = newest_row["title"] if newest_row["id"] != post_id else None

    md_text = markdown.Markdown(extenstions=['fenced_code'])
    body = md_text.convert(post['body'])
    title = post['title']
    date = post['created']

    return render_template('index.html',
                           body=body,
                           title=title,
                           date=date,
                           older_title=older_title,
                           newer_title=newer_title,
                           newest_title=newest_title)


@app.route('/resume')
def show_resume():
    """
    Show Eric's current resume
    """
    return render_template('resume.html')


@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(error: HTTPException) -> Tuple[Response, int]:
    """
    Handle 404 and 500 errors.

    Print the error and display an error page using the 'error.html' template.

    Args:
        error: The error object.

    Returns:
        A tuple containing the rendered error template and the error code.

    """
    print(f"ERROR: {error}")
    return render_template('error.html'), 404
