from flask import url_for, redirect

from flask_blog import app

from flask_login import logout_user


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
