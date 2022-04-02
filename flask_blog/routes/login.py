from flask import render_template, flash, redirect, url_for, session
from flask_blog import app
from flask_blog.forms import LoginForm


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
