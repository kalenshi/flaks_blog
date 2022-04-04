
from flask import url_for, redirect, flash

from flask_blog import app

from flask_login import logout_user, current_user


@app.route("/logout")
def logout():
    email = current_user.email
    logout_user()
    flash(message=f"Successfully logged out `{email}`", category="success")
    logout_user()
    return redirect(url_for("home"))
