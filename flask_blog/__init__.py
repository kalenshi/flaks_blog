import json
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_DIR = os.path.join(BASE_DIR, "config", "config.local.json")

with open(CONFIG_DIR, "r") as fh:
    config = json.load(fh)

app.config.update({"SECRET_KEY": config.get("SECRET_KEY")})
app.config.update(config.get("DATABASE"))
app.config.update(config.get("MAIL"))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flask_blog.users.routes import users
from flask_blog.posts.routes import posts
from flask_blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
