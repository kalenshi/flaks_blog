from flask import url_for, redirect, render_template, flash
from flask_login import current_user

from flask_blog.users.forms.request_reset_form import RequestRestForm
from flask_blog.models import User
from flask_blog.users.utils.send_email import send_email
from flask_blog.users.views import users_blueprint


@users_blueprint.route("/reset_request_password", methods=["POST", "GET"])
def reset_request_password():
    """

    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RequestRestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        send_email(user)
        flash("Check your email for a reset link!", category="success")
        return redirect(url_for("request_sent"))

    return render_template("request_reset_password.html", form=form)
