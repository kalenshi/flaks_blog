from flask import current_app
from flask_login import UserMixin
import datetime
import jwt

from extensions import db, login_manager, bcrypt

day_in_seconds = 24 * 60 * 60


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password, image_file="default.jpg"):
        self.username = username
        self.email = email
        self.image_file = image_file
        self.password = self.set_password(password)

    @staticmethod
    def set_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    def get_reset_token(self, exp=day_in_seconds):
        """
        Creates a token for the user
        :param exp:
        :return:
        """

        payload = {
            "user_id": self.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=exp)
        }
        token = jwt.encode(
            payload=payload,
            key=current_app.config.get("SECRET_KEY"),
            algorithm="HS256"
        )
        return token

    @staticmethod
    def verify_reset_token(token):
        try:
            serialized = jwt.decode(
                token,
                current_app.config.get("SECRET_KEY"),
                algorithms=["HS256"]
            )
            return User.query.get(serialized.get("user_id"))
        except jwt.ExpiredSignatureError:
            return None

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file})"
