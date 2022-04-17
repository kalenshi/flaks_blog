from ..views import errors_blueprint
from flask import render_template


@errors_blueprint.app_errorhandler(code=404)
def error_404(err):
    return render_template("404.html", err=err), 404


@errors_blueprint.app_errorhandler(code=403)
def error_403(err):
    return render_template("403.html", err=err), 403


@errors_blueprint.app_errorhandler(code=500)
def error_500(err):
    return render_template("500.html", err=err), 500
