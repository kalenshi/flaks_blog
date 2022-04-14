from flask import render_template

from flask_blog.users.views import users_blueprint


@users_blueprint.route("/request_sent", methods=["GET"])
def request_sent():
    return render_template("request_sent.html")
