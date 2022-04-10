from flask import render_template

from flask_blog.models import Post
from flask_blog.posts.routes import posts


@posts.route("/post/<int:post_id>", methods=["GET"])
def post(post_id):
    post_by_id = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post_by_id)
