# pylint: disable=C0411, C0413
"""
Create the Flask instance
"""
import os
from flask import Flask
from . import database


app = Flask(__name__)
from app import routes


app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'aeryck.sqlite'),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

database.init_app(app)
