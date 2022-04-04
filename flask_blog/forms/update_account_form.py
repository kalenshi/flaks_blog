from flask_wtf.form import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_login import current_user

from flask_blog.models import User


class UpdateAccountForm(FlaskForm):
    """
    This is the form for registering users on our site
    """
    username = StringField(label="Username", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    profile = FileField(label="Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField(label="Update")

    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(f"{email.data} is already registered.Use another email!")

    def validate_username(self, username):
        if current_user.username != username.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    f"{username.data} is already registered.Use another username!")
