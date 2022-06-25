"""
Create the Flask instance
"""
import os

from flask import Flask
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)
from app import routes

from . import database


app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'aeryck.sqlite'),
)

#if test_config is None:
#    app.config.from_pyfile('config.py', silent=True)
#else:
#    app.config.from_mapping(test_config)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

database.init_app(app)
