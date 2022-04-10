from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user

from flask_blog import db
from flask_blog.users.forms import UpdateAccountForm

from flask_blog.users.routes import users
from flask_blog.users.utils.save_picture import save_picture


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    posts = current_user.posts
    form = UpdateAccountForm()
    profile_image = url_for("static", filename=f"images/{current_user.image_file}")

    if form.validate_on_submit():
        if form.profile.data:
            profile_filename = save_picture(form.profile.data)
            current_user.image_file = profile_filename
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(message="Your account has been updated!", category="success")
        return redirect(url_for("users.account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template("account.html", form=form, profile_image=profile_image, posts=posts)
