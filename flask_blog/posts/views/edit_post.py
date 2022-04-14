from flask import flash, redirect, url_for, render_template, abort, request
from flask_login import login_required, current_user

from extensions import db
from flask_blog.posts.forms.create_post_form import CreatePostForm
from flask_blog.models import Post
from flask_blog.posts.views import posts_blueprint


@posts_blueprint.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    form = CreatePostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data

        db.session.commit()
        flash(message="Your post has been updated", category="success")
        return redirect(url_for("post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("../posts/templates/posts/update_post.html", form=form, legend="Update post")
