from flask import render_template
from flask_blog import app, bcrypt

from flask_blog.models import User
from flask_login import  login_required


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html")
