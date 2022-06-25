import os
import argparse
import sqlite3
from sqlite3 import Error


def get_filename():
    parser = argparse.ArgumentParser(description='Ingest a markdown file and'
                                            ' insert it into the database')
    parser.add_argument('FILENAME', help='Path to the markdown file to be'
                                        ' ingested')
    args = parser.parse_args()
    filename = args.FILENAME

    return filename


def create_connection(db_file) -> 'sqlite3.connect':
    database = None
    try:
        database = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return database


def read_post(filename) -> 'String':
    with open(filename) as f:
        text = f.readlines()

    return text


def ingest_file(filename) -> 'Tuple':
    title = str(os.path.basename(filename)).removesuffix('.md').replace('_', ' ')
    text = read_post(filename)
    body = ''
    for line in text:
        body += line

    return (title, body)


def insert_into_db(database, post):
    cursor = database.cursor()

    sql = ''' INSERT INTO post(title, body) VALUES(?,?) '''
    cursor.execute(sql,post)
    database.commit()


if __name__ == '__main__':
    filename = get_filename()
    database_file = r"instance/aeryck.sqlite"
    database = create_connection(database_file)
    ingested_file = ingest_file(filename)
    insert_into_db(database, ingested_file)
