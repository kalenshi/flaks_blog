from flask import url_for
from flask_mail import Message
from flask_blog import mail


def send_email(user):
    """
    Sends an email to then user
    :param user:
    :return:
    """
    token = user.get_reset_token()
    body = f"""
           To reset your password, visit the following link:
           {url_for("reset_password", token=token, _external=True)}
    """
    message = Message(
        subject="Reset password",
        recipients=[
            user.email,
        ],
        html=f"<div class='container'><h2>Please just follow the link</h2><p>{body}</p></div>",
        sender="kalenshi@gmial.com",

    )
    mail.send(message=message)
