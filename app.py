import os
import json
from flask import Flask, render_template, url_for, session, redirect, flash

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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    form_email = ""
    user = session.get("user")
    if user:
        form_email = user.get("email")

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data
        session["email"] = email
        if email == "kalenshi@gmail.com" and password == "123":
            flash(message="You have been logged in!", category="success")
            return redirect(location=url_for('home'))
        else:
            flash(message="Invalid credentials!", category="danger")
    return render_template("login.html", form=form, form_email=form_email)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(message="Thank you for Registering!", category="success")
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        session["user"] = {
            "username": username,
            "email": email,
            "password": password
        }
        return redirect(location=url_for("login"))
    return render_template("register.html", form=form)


@app.errorhandler(404)
def page_not_found(err):
    return render_template("page_not_found.html", err=err), 404


if __name__ == "__main__":
    app.run(debug=True)
