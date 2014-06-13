from app import app
from app.models import Post, Page
from flask import render_template, url_for, send_from_directory


@app.route('/')
@app.route('/index')
def index():
    posts = Post.objects(published=True)
    return render_template("index.html", posts=posts)


@app.route('/<url>')
def page(url):
    page = Page.objects.get_or_404(url=url)
    return render_template("post.html", post=page)


@app.route('/post/<slug>')
def post(slug):
    post = Post.objects.get_or_404(slug=slug)
    return render_template("post.html", post=post)
