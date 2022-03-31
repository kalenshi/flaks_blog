from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """
    This is the form for registering users on our site
    """
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), ])
    remember = BooleanField(label="Remember Me")
    submit = SubmitField(label="Login")
