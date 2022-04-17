from flask import render_template
from flask_blog.public.views import public_blueprint


@public_blueprint.route("/biography")
def biography():
    return render_template("biography.html")
