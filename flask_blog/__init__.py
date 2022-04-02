import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from flask_blog.routes import *

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config.update({
    "SECRET_KEY": os.environ.get("FLASK_SECRET", "ab7b554b5251a4592ba966e44cc2daac"),
    "SQLALCHEMY_DATABASE_URI": "sqlite:///site.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

db = SQLAlchemy(app)
