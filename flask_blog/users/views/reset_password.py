from flask import url_for, redirect, render_template, flash
from flask_login import current_user

from extensions import db
from flask_blog.users.forms.reset_password_form import ResetPasswordForm
from flask_blog.models import User
from flask_blog.users.views import users_blueprint


@users_blueprint.route("/reset_password/<string:token>", methods=["POST", "GET"])
def reset_password(token):
    """

    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    user = User.verify_reset_token(token)
    if not user:
        flash("That is an invalid or expired token", category="warning")
        return redirect(url_for("users_blueprint.reset_request_password"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # extra unnecessary check
        if form.password.data == form.confirm_password.data:
            user.password = User.set_password(form.password.data)
            db.session.commit()
            flash(
                "Your password was successfully Reset! Login with your new password",
                category="success"
            )
            return redirect(url_for("users_blueprint.login"))
    return render_template("reset_password.html", form=form)
