from flask import render_template

from flask_blog.public.views import public_blueprint


@public_blueprint.errorhandler(404)
def page_not_found(err):
    message = f"{err.name}: {err.description.split('.')[0]}"
    return render_template("page_not_found.html", message=message), err.code
