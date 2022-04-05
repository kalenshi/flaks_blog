from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CreatePostForm(FlaskForm):
    """
    This is the form for users to create new posts
    """
    title = StringField(label="Title", validators=[DataRequired(), ])
    content = TextAreaField(label="Content", validators=[DataRequired(), ])

    submit = SubmitField(label="Post")
