import argparse
import sqlite3
from pathlib import Path
from sqlite3 import Error

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.r import SLexer
from pygments.lexers.sql import PostgresLexer
from pygments.formatters import HtmlFormatter


def parse_args():
    parser = argparse.ArgumentParser(description='Ingest a markdown file and'
                                            ' insert it into the database')
    parser.add_argument('FILENAME', help='Path to the markdown file to be'
                                        ' ingested')
    parser.add_argument('-u', '--update', action='store_true',
                        help='If enabled, update an existing post instead of '
                        'creating a new one')
    args = parser.parse_args()
    filepath = Path(args.FILENAME)

    return filepath, args.update


def create_connection(db_file) -> 'sqlite3.connect':
    database = None
    try:
        database = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return database


def read_post(path) -> 'String':
    with path.open() as f:
        text = f.readlines()

    return text


def ingest_file(path) -> 'Tuple':
    title = path.stem.removesuffix('.md').replace('_', ' ')
    text = read_post(path)
    body = ''
    code_block = ''
    language = None
    in_code_block = False
    for line in text:
        if line.startswith("```"):
            in_code_block = not(in_code_block)
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


def insert_into_db(database, post, update=False):
    cursor = database.cursor()

    if update:
        sql = ''' UPDATE post SET body = (?) WHERE title = (?) '''
    else:
        new_post_id = cursor.execute("SELECT COALESCE(MAX(id), 0) "\
                                     "FROM post").fetchone()[0] + 1
        post = (new_post_id, *post)
        sql = ''' INSERT INTO post(id, body, title) VALUES(?,?,?) '''
    cursor.execute(sql, post)
    database.commit()


if __name__ == '__main__':
    filepath, update = parse_args()
    database_file = r"instance/aeryck.sqlite"
    database = create_connection(database_file)

    ingested_file = ingest_file(filepath)
    insert_into_db(database, ingested_file, update=update)
