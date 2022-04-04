from flask import flash, redirect, url_for, render_template
from flask_login import current_user

from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm
from flask_blog.models import User


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data == form.confirm_password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_password
            )
            db.session.add(user)
            db.session.commit()
            flash("Your account has been created! You can now log in", "success")
        return redirect(location=url_for("login"))
    return render_template("register.html", form=form)
