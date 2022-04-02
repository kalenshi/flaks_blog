from flask import flash, redirect, url_for, session, render_template

from flask_blog import app
from flask_blog.forms import RegistrationForm


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
