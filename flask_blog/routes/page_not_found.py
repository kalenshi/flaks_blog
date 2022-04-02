from flask import render_template

from flask_blog import app


@app.errorhandler(404)
def page_not_found(err):
    return render_template("page_not_found.html", err=err), 404
