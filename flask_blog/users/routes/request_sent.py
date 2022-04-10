from flask import render_template

from flask_blog.users.routes import users


@users.route("/request_sent", methods=["GET"])
def request_sent():
    return render_template("request_sent.html")
