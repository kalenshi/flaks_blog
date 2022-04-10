from flask_blog import db, login_manager, bcrypt, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as TokenSerializer, SignatureExpired

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

    def get_reset_token(self, expires_in_secs=60):
        """
        Creates a token for the user
        :param expires_in_secs:
        :return:
        """
        token_serializer = TokenSerializer(
            secret_key=app.config.get("SECRET_KEY"),
            expires_in=expires_in_secs
        )
        token = token_serializer.dumps({"user_id": self.id}).decode("utf-8")
        return token

    @staticmethod
    def verify_reset_token(token_hash):
        token_serializer = TokenSerializer(secret_key=app.config.get("SECRET_KEY"))
        try:
            user_id = token_serializer.loads(token_hash).get("user_id")
            return User.query.get(user_id)
        except SignatureExpired:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file})"
