from flask import render_template
from flask_blog.public.views import public_blueprint


@public_blueprint.route("/about")
def about():
    return render_template("about.html")
