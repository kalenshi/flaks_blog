import os
from flask import Blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

template_folder = os.path.join(BASE_DIR, "templates", "public")

public_blueprint = Blueprint("public_blueprint", __name__, template_folder=template_folder)
