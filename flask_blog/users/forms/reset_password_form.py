from flask_wtf.form import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class ResetPasswordForm(FlaskForm):
    """
    This is the form for Rest users password
    """

    password = PasswordField(label="New Password", validators=[DataRequired(), ])
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), EqualTo(fieldname="password"), Length(min=6, max=50)]
    )

    submit = SubmitField(label="Reset Password")
