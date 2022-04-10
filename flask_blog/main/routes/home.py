from flask import render_template, request

from flask_blog.main.routes import main
from flask_blog.models import Post

per_page = 4


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=per_page, page=page)

    return render_template("home.html", posts=posts)
