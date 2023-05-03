"""
Connect to the database

Methods
-------
get_database() -> g.database
    Fetch the database instance.

close_database()
    Close the database.
"""
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_database() -> 'g.database':
    """
    Fetch the database instance.

    Attributes
    ----------
    g : Flask object
        'g' is a Flask object that is unique for each request and used to store
        data.

        database : sqlite3 connection
            The backend database for aeryck.com
    """
    if 'database' not in g:
        g.database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.database.row_factory = sqlite3.Row

    return g.database


def close_database(error=None):
    """
    Close the database

    Attributes
    ----------
    database : sqlite3 conneciton
        The backend database for aeryck.com
    """
    if error:
        print(f'ERROR in close_database: {error}')
    database = g.pop('database', None)

    if database is not None:
        database.close()


def init_database():
    """
    Create the database instance.

    Attributes
    ----------
    database : sqlite3 conneciton
        The backend database for aeryck.com
    """
    database = get_database()

    with current_app.open_resource('schema.sql') as schema:
        database.executescript(schema.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    (re)initialize the database

    Attributes
    ----------
    warning_response : String
        The user will be asked to confirm if they want to drop and
        re-initialize the database. Their response is stored in this variable.
    """
    warning_response = input("WARNING: This will reset the database, are you "
        "sure you want to continue? [y/N]: ")
    if warning_response in ('y', 'Y'):
        init_database()
        click.echo('Database initialized.')


def init_app(app):
    """
    Initialize the application.
    """
    app.teardown_appcontext(close_database)
    app.cli.add_command(init_db_command)
