from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    This is the form for registering users on our site
    """
    username = StringField(label="Username", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), ])
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(),
                    EqualTo(fieldname="password")]
    )
    submit = SubmitField(label="Register")

