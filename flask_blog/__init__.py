import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config.update({
    "SECRET_KEY": os.environ.get("FLASK_SECRET", "ab7b554b5251a4592ba966e44cc2daac"),
    "SQLALCHEMY_DATABASE_URI": "sqlite:///site.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flask_blog.routes import *
