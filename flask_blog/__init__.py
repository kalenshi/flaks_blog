import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required
from flask_mail import Mail

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config.update({
    "SECRET_KEY": os.environ.get("FLASK_SECRET", "ab7b554b5251a4592ba966e44cc2daac"),
    "SQLALCHEMY_DATABASE_URI": "sqlite:///site.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "MAIL_PORT": 465,
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_USERNAME": "kalenshi@gmail.com",
    "MAIL_PASSWORD": "cxcnehapxfnutfij",
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True

})

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flask_blog.routes import *
