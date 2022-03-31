import os
import json
from flask import Flask, render_template, url_for

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config.update({
    "SECRET_KEY": os.environ.get("FLASK_SECRET", "ab7b554b5251a4592ba966e44cc2daac"),
})

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

posts_path = os.path.join(TEMPLATES_DIR, "posts.json")

with open(posts_path, "r") as fh:
    posts = json.load(fh)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form=form)


@app.errorhandler(404)
def page_not_found(err):
    return render_template("page_not_found.html", err=err), 404


if __name__ == "__main__":
    app.run(debug=True)
