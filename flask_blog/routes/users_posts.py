from flask import render_template, request

from flask_blog import app
from flask_blog.models import User, Post

per_page = 3


@app.route("/user/<string:username>", methods=["GET", "POST"])
def user_posts(username=None):
    page = request.args.get("page", default=1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).paginate(per_page=per_page, page=page)

    return render_template("user_posts.html", posts=posts, user=user)
