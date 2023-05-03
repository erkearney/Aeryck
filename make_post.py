"""
This script ingests a markdown file and inserts it into a SQLite database. It
reads a markdown file and extracts its title and body, highlighting code blocks
with Pygments. The resulting post is then inserted into the database, either as
a new post or as an update to an existing one.

Usage:
    To run the script, call the script with the path to the markdown file as the
    first argument. By default, the script will create a new post in the
    database. To update an existing post, use the `-u` or `--update` flag.

Dependencies:
    - argparse
    - pathlib
    - sqlite3
    - pygments

Example:
    `python ingest.py my_post.md`: Insert a new post into the database
    `python ingest.py my_post.md -u`: Update an old post in the database
        (NOTE: this will NOT update the post_date)

Functions:
    - parse_args(): Parse command line arguments.
    - create_connection(db_file: str) -> sqlite3.Connection: Create a connection
        to a SQLite database.
    - read_post(path: Path) -> str: Read the contents of a file.
    - ingest_file(path: Path) -> tuple: Parse a markdown file and extract its
        title and body.
    - insert_into_db(database_conn: sqlite3.Connection, post: tuple,
        update: bool = False) -> None: Insert a post into the database.

For more information on Pygments, see: https://pygments.org/
For more information on SQLite, see: https://www.sqlite.org/
"""
import argparse
import sqlite3
from pathlib import Path
from sqlite3 import Error

from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.lexers.r import SLexer
from pygments.lexers.sql import PostgresLexer
from pygments.formatters.html import HtmlFormatter


def parse_args() -> tuple:
    """
    Parse command line arguments.

    Args:
        None.

    Returns:
        A tuple containing a Path object for the input file and a boolean flag indicating
        whether to update an existing post instead of creating a new one.

    Raises:
        None.
    """
    parser = argparse.ArgumentParser(description='Ingest a markdown file and'
                                            ' insert it into the database')
    parser.add_argument('FILENAME', help='Path to the markdown file to be'
                                        ' ingested')
    parser.add_argument('-u', '--update', action='store_true',
                        help='If enabled, update an existing post instead of '
                        'creating a new one')
    args = parser.parse_args()

    return Path(args.FILENAME), args.update


def create_connection(db_file: str) -> sqlite3.Connection:
    """
    Create a connection to a SQLite database.

    Args:
        db_file: A string containing the path to the database file.

    Returns:
        A Connection object to the database.

    Raises:
        Error: If there was an error creating the connection to the database.
    """
    db_conn = None
    try:
        db_conn = sqlite3.connect(db_file)
    except Error as err:
        print(err)

    return db_conn


def read_post(path: Path) -> str:
    """
    Read the contents of a file.

    Args:
        path: A Path object representing the path to the file.

    Returns:
        A string containing the contents of the file.

    Raises:
        None.
    """
    with path.open() as file:
        markdown_text = file.readlines()

    return markdown_text


def ingest_file(path: Path) -> tuple:
    """
    Parse a markdown file and extract its title and body.

    Args:
        path: A Path object representing the path to the file.

    Returns:
        A tuple containing the body of the file (with code blocks highlighted) and its title.

    Raises:
        None.
    """
    title = path.stem.removesuffix('.md').replace('_', ' ')
    text = read_post(path)
    body = ''
    code_block = ''
    language = None
    in_code_block = False
    for line in text:
        if line.startswith("```"):
            in_code_block = not in_code_block
            if "python" in line:
                language = "python"
            elif "r" in line:
                language = "R"
            elif "sql" in line:
                language = "SQL"
            continue

        if in_code_block:
            code_block += line
        elif code_block:
            if language == "python":
                body += highlight(code_block, PythonLexer(), HtmlFormatter())
            elif language == "R":
                body += highlight(code_block, SLexer(), HtmlFormatter())
            elif language == 'SQL':
                body += highlight(code_block, PostgresLexer(), HtmlFormatter())
            else:
                body += code_block
            code_block = ''
        else:
            body += line

    return (body, title)


def insert_into_db(database_conn: sqlite3.Connection, post: tuple,
                   update_post: bool = False) -> None:
    """
    Insert a post into the database.

    Args:
        database_conn: A Connection object to the database.
        post: A tuple containing the body and title of the post.
        update_post: A boolean flag indicating whether to update an existing
            post or create a new one.

    Returns:
        None.

    Raises:
        None.
    """
    cursor = database_conn.cursor()

    if update_post:
        sql = ''' UPDATE post SET body = (?) WHERE title = (?) '''
    else:
        new_post_id = cursor.execute("SELECT COALESCE(MAX(id), 0) "\
                                     "FROM post").fetchone()[0] + 1
        post = (new_post_id, *post)
        sql = ''' INSERT INTO post(id, body, title) VALUES(?,?,?) '''
    cursor.execute(sql, post)
    database_conn.commit()


if __name__ == '__main__':
    filepath, update = parse_args()
    DATABSE_FILE = r"instance/aeryck.sqlite"
    database_connection = create_connection(DATABSE_FILE)

    ingested_file = ingest_file(filepath)
    insert_into_db(database_connection, ingested_file, update_post=update)
