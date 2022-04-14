import os
from flask import Blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

template_folder = os.path.join(BASE_DIR, "templates", "posts")

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder=template_folder)
