import os
from flask import Blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

template_folder = os.path.join(BASE_DIR, "templates", "users")

users_blueprint = Blueprint("users_blueprint", __name__, template_folder=template_folder)
