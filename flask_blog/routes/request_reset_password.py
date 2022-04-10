from flask import url_for, redirect, render_template, flash, request
from flask_login import current_user
from flask_mail import Message

from flask_blog import app, mail
from flask_blog.forms.request_reset_form import RequestRestForm
from flask_blog.models import User
from flask_blog.utils.send_email import send_email


@app.route("/reset_request_password", methods=["POST", "GET"])
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
