from flask import render_template
from flask_blog import app
from flask_blog.models import Post


@app.route("/post/<int:post_id>", methods=["GET"])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)
