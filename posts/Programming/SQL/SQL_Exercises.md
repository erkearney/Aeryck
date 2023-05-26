Welcome to the end of this SQL tutorial! This post contains various exercises
designed to test your understanding.

### [Basic Data Manipulation](https://aeryck.com/post:SQL Basic Data Manipulation)
### [Joins and Relationships](https://aeryck.com/post:SQL Intermediate Querying and Joins)
### [Primary and Foreign Keys](https://aeryck.com/post:SQL Primary and Foreign Keys)
### [Transactions and ACID properties](https://aeryck.com/post:SQL%20Transactions%20and%20ACID%20properties)
### [Views Procedures and Functions](https://aeryck.com/post:SQL Views Procedures and Functions)
### [Exercises (this post)](https://aeryck.com/post:SQL Views Procedures and Functions)

## A word on 'difficulty'
These exercises are sorted into three difficulties:

- Introductory: The solutions to these exercises are very similar to examples
  given throughout this tutorial. If you find yourself struggling with these
  exercises I'd advise to re-read the relevant post(s).
- Intermediate: The tools required for the solutions to these exercises are
  provided within this tutorial, but you'll need to use them in new and creative
  ways. 
- Challenging: You will need to use resources outside this tutorial to solve
  these exercises. Please be aware the fact you'll need to use use techniques
  not covered within this tutorial is **100% intentional**, as they are designed
  to test your ability to learn more about SQL on your own. This tutorial was
  meant to provide the foundational skills you'll need, not be an exhaustive
  resource covering everything!

The solutions to each exercise are short (<=20 lines). I'd suggest you try to
complete each exercise without hints first, using them only if you've been
'stuck' for more than two minutes.

To start, run the following commands in your own database:

```sql
DROP TABLE IF EXISTS books;

CREATE TABLE books (
  book_id SERIAL PRIMARY KEY,
  title VARCHAR(100),
  author VARCHAR(30),
  year_published INT,
  genre VARCHAR(30)
);

INSERT INTO books (title, author, year_published, genre)
VALUES ('A Tale of Two Cities', 'Charles Dickens', 1859, 'Historical fiction'),
       ('And Then There Were None', 'Agatha Christie', 1939, 'Mystery'),
       ('The Hobbit', 'J. R. R. Tolkien', 1937, 'Fantasy'),
       ('Harry Potter and the Philosopher''s Stone', 'J. K. Rowling', 1997, 'Fantasy'),
       ('The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 1950, 'Fantasy');
```

###### (Note the use of double apostrophe '' to escape the ' in Philosopher's)

## Introductory
#### These exercises should be trivial if you've read this full tutorial.
* * *
1: SELECT all the 'Fantasy' books from the *books* table, sort them from oldest
to newest.

Expected result:

<table border="1">
  <tr>
    <th align="center">title</th>
    <th align="center">author</th>
    <th align="center">year_published</th>
    <th align="center">genre</th>
  </tr>
  <tr valign="top">
    <td align="left">The Hobbit</td>
    <td align="left">J. R. R. Tolkien</td>
    <td align="right">1937</td>
    <td align="left">Fantasy</td>
  </tr>
  <tr valign="top">
    <td align="left">The Lion, the Witch and the Wardrobe</td>
    <td align="left">C. S. Lewis</td>
    <td align="right">1950</td>
    <td align="left">Fantasy</td>
  </tr>
  <tr valign="top">
    <td align="left">Harry Potter and the Philosopher's Stone</td>
    <td align="left">J. K. Rowling</td>
    <td align="right">1997</td>
    <td align="left">Fantasy</td>
  </tr>
</table>
<p>(3 rows)<br />
</p>

<details>
<summary>Hint(s)</summary>
Relevant post: <a
href="https://aeryck.com/post:SQL%20Basic%20Data%20Manipulation">Basic Data
Manipulation</a><br><br>


Keywords needed: SELECT, FROM, WHERE, ORDER BY
</details>

<details>
<summary>Solution</summary>

```sql
SELECT title, author, year_published, genre
  FROM books
 WHERE genre = 'Fantasy'
 ORDER BY year_published;
```

</details>

* * *
2: Change the title of "Harry Potter and the Philosopher's Stone" to "Harry
Potter and the Sorcerer's Stone". (Remember you'll need to escape the apostrophe
in Sorcerer's as 'Sorcerer''s'). Then add the following new books:

- title: The Da Vanci Code, author: Dan Brown, year_published: 2003, genre:
  Mystery
- title: The Catcher in the Rye, author: J. D. Salinger, year_published: 1951,
  genre: Coming-of-age

Finally, output just the titles of all books in the *books* table (no additional
columns), sorted alphabetically by title.

Expected result:

<table border="1">
  <tr>
    <th align="center">title</th>
  </tr>
  <tr valign="top">
    <td align="left">And Then There Were None</td>
  </tr>
  <tr valign="top">
    <td align="left">A Tale of Two Cities</td>
  </tr>
  <tr valign="top">
    <td align="left">Harry Potter and the Sorcerer's Stone</td>
  </tr>
  <tr valign="top">
    <td align="left">The Catcher in the Rye</td>
  </tr>
  <tr valign="top">
    <td align="left">The Da Vinci Code</td>
  </tr>
  <tr valign="top">
    <td align="left">The Hobbit</td>
  </tr>
  <tr valign="top">
    <td align="left">The Lion, the Witch and the Wardrobe</td>
  </tr>
</table>
<p>(7 rows)<br />
</p>

<details>
<summary>Hint(s)</summary>
Relevant post: <a
href="https://aeryck.com/post:SQL%20Basic%20Data%20Manipulation">Basic Data
Manipulation</a><br><br>

Keywords needed: SELECT, FROM, WHERE, ORDER BY, UPDATE, SET, INSERT INTO, VALUES
</details>

<details>
<summary>Solution</summary>

```sql
UPDATE books SET title = 'Harry Potter and the Sorcerer''s Stone'
 WHERE title = 'Harry Potter and the Philosopher''s Stone';

INSERT INTO books (title, author, year_published, genre)
VALUES ('The Da Vinci Code', 'Dan Brown', 2003, 'Mystery'),
       ('The Catcher in the Rye', 'J. D. Salinger', 1951, 'Coming-of-age');

SELECT title FROM books
 ORDER BY title;
```

</details>

* * *
3: Create a new table called *authors*, give it the following columns. Make the
datatype of each column VARCHAR(30). Make the **penname** column a PRIMARY KEY.

- penname
- first_name
- middle_name
- last_name
- nationality

Now add the following data to the *authors* table:

- penname: J. R. R. Tolkien, first_name: John, middle_name: Ronald Reuel,
  last_name: Tolkien, nationality: English
- penname: Dan Brown, first_name: Daniel, middle_name: Gerhard, last_name:
  Brown, nationality: American

Finally, output only the titles of books and the nationalities of their authors.

Expected result:

<table border="1">
  <tr>
    <th align="center">title</th>
    <th align="center">nationality</th>
  </tr>
  <tr valign="top">
    <td align="left">The Da Vinci Code</td>
    <td align="left">American</td>
  </tr>
  <tr valign="top">
    <td align="left">The Hobbit</td>
    <td align="left">English</td>
  </tr>
</table>
<p>(2 rows)<br />
</p>

<details>
<summary>Hint(s)</summary>
Relevant posts: <a
href="https://aeryck.com/post:SQL%20Basic%20Data%20Manipulation">Basic Data
Manipulation</a><br><br>

<a href="https://aeryck.com/post:SQL%20Intermediate%20Querying%20and%20Joins">
Intermediate Querying and Joins</a><br><br>

<a href="https://aeryck.com/post:SQL%20Primary%20and%20Foreign%20Keys">
Primary and Foreign Keys</a><br><br>

Keywords needed: SELECT, FROM, INSERT INTO, VALUES, CREATE TABLE, PRIMARY KEY,
AS, JOIN, VARCHAR
</details>

<details>
<summary>Solution</summary>

```sql
CREATE TABLE authors (penname VARCHAR(30) PRIMARY KEY,
                      first_name VARCHAR(30),
                      middle_name VARCHAR(30),
                      last_name VARCHAR(30),
                      nationality VARCHAR(30)
);

INSERT INTO authors(penname, first_name, middle_name, last_name, nationality)
VALUES ('J. R. R. Tolkien', 'John', 'Ronald Reuel', 'Tolkien', 'English'),
       ('Dan Brown', 'Daniel', 'Gerhard', 'Brown', 'American');

SELECT b.title, a.nationality
  FROM books AS b
       JOIN authors AS a ON b.author = a.penname;
```

</details>

* * *
4: Make the **author** column in the *books* table a foreign key that references
the **penname** column of *authors*. Set it so that changes made to **penname**
in *authors* will be reflected in **author** in *books*.

<details>
<summary>Hint(s)</summary>
Relevant post: <a
href="https://aeryck.com/post:SQL%20Primary%20and%20Foreign%20Keys">Primary and
Foreign Keys</a><br><br>

Keywords needed: ALTER TABLE, ADD CONSTRAINT, FOREIGN KEY, REFERENCES, ON
UPDATE, CASCADE
</details>

<details>
<summary>Solution</summary>

```sql
     ALTER TABLE books
       ADD CONSTRAINT fk_books_authors
   FOREIGN KEY (author)
REFERENCES authors(penname)
 ON UPDATE CASCADE;
```

</details>

## Intermediate
#### You'll have all the tools you'll need to solve these exercises if you've read this tutorial, but you'll need to apply them in new and creative ways.

#### These questions are related to procedures and functions, meaning there will be syntactical differences between different database management systems. The provided solutions were written for PostgreSQL.

* * *
5: Create a new table called *library_users* with two columns: **user_id** and
**first_name**. Make **user_id** an integer, make it automatically increment
with each new row, and make it a primary key, make **first_name** a VARCHAR(30).
Add two users, 'Alice' and 'Bob'. Next, add a new column to *books* called
**checked_out_by**, and make it a foreign key that references the **user_id**
column of *library_users*. Leave **checked_out_by** column empty for now. As
with question 4, you can write this yourself or use the provided statements to
do the work for you:

<details>
<summary>Create library_users table and add checked_out_by to books</summary>

```sql
DROP TABLE IF EXISTS library_users

CREATE TABLE library_users (
  user_id SERIAL PRIMARY KEY
  first_name VARCHAR(30)
);

INSERT INTO library_users (first_name)
VALUES ('Alice'),
       ('Bob');

    ALTER TABLE books
      ADD checked_out_by INT;
      ADD CONSTRAINT fk_books_library_user
  FOREIGN KEY (checked_out_by)
REFERENCES library_users(user_id);
```

</details>

Now, write a procedure called check_out_book which takes two arguments: user_id
and checkout_book_id. The procedure should update the **checked_out_by** column
of the appropriate book with the user's id. Don't worry about edge cases (e.g.,
id numbers being supplied that don't exist).

Test your new procedure by having Alice check out 'A Tale of Two Cities' and Bob
check out 'The Lion, the Witch, and the Wardrobe'.

Finally, create a view with two columns: the first being the **title** of all
books currently checked out, and the second being the **first_name** of the user
who currently has the book checked out. Use an alias on the second column to
change its name to 'checked out by'.

Expected result:

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">title</th>
  </tr>
  <tr valign="top">
    <td align="left">Alice</td>
    <td align="left">A Tale of Two Cities</td>
  </tr>
  <tr valign="top">
    <td align="left">Bob</td>
    <td align="left">The Lion, the Witch and the Wardrobe</td>
  </tr>
</table>
<p>(2 rows)<br />
</p>

<details>
<summary>Hint(s)</summary>
Relevant posts: <a
href="https://aeryck.com/post:SQL%20Views%20Procedures%20and%20Functions">Views
Procedures and Functions</a><br><br>

<a
href="https://aeryck.com/post:SQL%20Intermediate%20Querying%20and%20Joins">Intermediate
Querying and Joins</a><br><br>

Keywords needed: SELECT, FROM, JOIN, AS, CREATE PROCEDURE, LANGUAGE, plpgsql,
BEGIN, END, UPDATE, WHERE, SET, COMMIT, CALL, CREATE VIEW, INT
</details>

<details>
<summary>Solution</summary>

```sql
  CREATE PROCEDURE check_out_book (user_id INT,
                                   checkout_book_id INT)
LANGUAGE plpgsql
      AS $$
   BEGIN
         UPDATE books
            SET checked_out_by = user_id
          WHERE book_id = checkout_book_id;
         COMMIT;
     END;
      $$;

CALL check_out_book(1, 1);
CALL check_out_book(2, 5);

CREATE VIEW checked_out_books AS
SELECT u.first_name, b.title
  FROM books AS b
       JOIN library_users AS u ON b.checked_out_by = u.user_id;

SELECT * FROM checked_out_books;
```

</details>

* * *

6: Write a function called get_num_books_checked_out which takes one argument:
first_name, and outputs the number of books checked out by that user. Test this
by calling

```sql
SELECT count_num_books_checked_out ('Alice') AS num_books;
```

Expected result:

<table border="1">
  <tr>
    <th align="center">count_num_books_checked_out</th>
  </tr>
  <tr valign="top">
    <td align="right">1</td>
  </tr>
</table>
<p>(1 row)<br />
</p>

<details>
<summary>Hint(s)</summary>
Relevant posts: <a
href="https://aeryck.com/post:SQL%20Views%20Procedures%20and%20Functions">Views
Procedures and Functions</a><br><br>

Keywords needed: CREATE FUNCTION, RETURNS, RETURN, LANGUAGE, BEGIN, AS, SELECT,
FROM, WHERE, VARCHAR
</details>

<details>
<summary>Solution</summary>

```sql
  CREATE FUNCTION count_num_books_checked_out (user_first_name VARCHAR)
 RETURNS INT
LANGUAGE plpgsql
      AS $$
DECLARE
         this_user_id INT;
         result INT;
  BEGIN
         SELECT user_id INTO this_user_id
           FROM library_users
          WHERE first_name = user_first_name;

         SELECT COUNT(*) INTO result
           FROM books
          WHERE checked_out_by = this_user_id;

         RETURN result;
    END;
     $$;

SELECT count_num_books_checked_out ('Alice') AS num_books;
```

</details>

* * *
## Challenging
#### You will need to seek resources outside this tutorial, or use the tools within this tutorial in **very** creative ways to solve these exercises

7: Update the check_out_book procedure from question 5 to check if the book has
already been checked out by another user, and if it has, raise a notice of the
form "book_id: `<the book id`> has already been checked out by user:
`<user id`>.

<details>
<summary>Hint(s)</summary>
- The keywords you'll need to learn about are IF, ELSE, and RAISE NOTICE

- You'll need to create another variable within the function
</details>

<details>
<summary>Solution</summary>

```sql
  CREATE OR REPLACE PROCEDURE check_out_book (user_id INT,
                                              checkout_book_id INT)
LANGUAGE plpgsql
      AS $$ DECLARE already_checked_out_by INT;
   BEGIN
     SELECT checked_out_by INTO already_checked_out_by
       FROM books
      WHERE book_id = checkout_book_id;

       IF already_checked_out_by IS NOT NULL THEN
          RAISE NOTICE 'Book_id: % is already checked out by user: %', checkout_book_id, already_checked_out_by;
     ELSE
          UPDATE books
             SET checked_out_by = user_id
           WHERE book_id = checkout_book_id; END IF;
          COMMIT;
     END;
      $$;
```

</details>

8: Run the following query to insert multiple copies of the same book into
the *books* table:

```sql
INSERT INTO books (title, author, year_published, genre)
VALUES ('The Lord of the Rings', 'J. R. R. Tolkien', 1955, 'Fantasy'),
       ('The Lord of the Rings', 'J. R. R. Tolkien', 1955, 'Fantasy'),
       ('The Lord of the Rings', 'J. R. R. Tolkien', 1955, 'Fantasy'),
       ('The Lord of the Rings', 'J. R. R. Tolkien', 1955, 'Fantasy'),
       ('The Lord of the Rings', 'J. R. R. Tolkien', 1955, 'Fantasy'),
       ('The Lord of the Rings', 'J. R. R. Tolkien', 1955, 'Fantasy');
```

Remove the duplicate copies from the *books* table, leaving only one row. Do
this without using a temporary table.

<details>
<summary>Hint(s)</summary>
You won't need any new keywords to do this, instead you'll need to learn about
subqueries.
</details>

<details>
<summary>Solution</summary>

```sql
DELETE FROM books
 WHERE book_id NOT IN (
    SELECT MIN(book_id)
      FROM books
     GROUP BY title, author, year_published, genre
);
```

</details>

And that concludes this SQL tutorial! There is still much to explore, including
trying different database systems, learning about query optimization, backing
up and restoring the database, protecting from SQL injection, etc. That being
said you should now have the foundational skills necessary to be able to teach
yourself any of these topics, and more!
