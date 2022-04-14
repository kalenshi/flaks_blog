from flask import render_template, request

from flask_blog.models import Post
from flask_blog.public.views import public_blueprint

per_page = 4


@public_blueprint.route("/")
@public_blueprint.route("/home")
def home():
    page = request.args.get("page", default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=per_page, page=page)

    return render_template("home.html", posts=posts)
