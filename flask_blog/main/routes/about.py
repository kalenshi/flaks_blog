from flask import render_template

from flask_blog.main.routes import main


@main.route("/about")
def about():
    return render_template("about.html")
