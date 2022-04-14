from flask import render_template

from flask_blog.models import Post
from flask_blog.posts.views import posts_blueprint


@posts_blueprint.route("/post/<int:post_id>", methods=["GET"])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("../posts/templates/posts/post.html", post=post)
