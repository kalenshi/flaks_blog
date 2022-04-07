from flask import render_template, flash, redirect, url_for, session, request
from werkzeug.urls import url_parse

from flask_blog import app, bcrypt
from flask_blog.forms import LoginForm
from flask_blog.models import User
from flask_login import login_user, current_user


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            print("------------------------------------------------------")
            print(next_page)
            print(url_parse(next_page).netloc)
            print("------------------------------------------------------")
            if next_page and next_page.startswith("/"):
                next_page = next_page[1:]
            return redirect(url_for(next_page)) if next_page else redirect(url_for("home"))

        else:
            flash(message="Invalid credentials!", category="danger")
    return render_template("login.html", form=form)
