from flask import render_template
from flask_blog import app
from flask_blog.models import Post


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)
