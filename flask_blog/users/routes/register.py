from flask import flash, redirect, url_for, render_template
from flask_login import current_user

from flask_blog import db
from flask_blog.models import User
from flask_blog.users.forms import RegistrationForm
from flask_blog.users.routes import users


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data == form.confirm_password.data:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            flash("Your account has been created! You can now log in", "success")
        return redirect(location=url_for("users.login"))
    return render_template("register.html", form=form)
