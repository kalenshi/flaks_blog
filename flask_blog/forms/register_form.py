from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask_blog.models import User


class RegistrationForm(FlaskForm):
    """
    This is the form for registering users on our site
    """
    username = StringField(label="Username", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), ])

    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(fieldname="password"),
            Length(min=6, max=50)
        ]
    )
    submit = SubmitField(label="Register")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(f"{email.data} is already registered.Use another email!")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError(f"{username.data} is already registered.Use another username!")
