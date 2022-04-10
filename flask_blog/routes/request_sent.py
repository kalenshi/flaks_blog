from flask import render_template
from flask_blog import app


@app.route("/request_sent", methods=["GET"])
def request_sent():
    return render_template("request_sent.html")
