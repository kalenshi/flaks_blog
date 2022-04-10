from flask_wtf.form import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, ValidationError

from flask_blog.models import User


class RequestRestForm(FlaskForm):
    """
    This is the form for Rest users password
    """

    email = EmailField(label="Email", validators=[DataRequired(), ])
    submit = SubmitField(label="Request Password Reset")

    def validate_email(self, email):
        """
        If the email exists in the database, then send a reset token
        otherwise, throw an invalid data exception
        :param email:
        :return:
        """
        if not User.query.filter_by(email=email.data).first():
            raise ValidationError("There is no account with that email")
