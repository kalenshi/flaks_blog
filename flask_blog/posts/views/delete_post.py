from flask import flash, redirect, url_for, abort
from flask_login import login_required, current_user

from extensions import db
from flask_blog.models import Post
from flask_blog.posts.views import posts_blueprint


@posts_blueprint.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", category="success")
    return redirect(url_for("public_blueprint.home"))
