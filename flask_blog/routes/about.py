from flask import render_template
from flask_blog import app


@app.route("/about")
def about():
    return render_template("about.html")
