from app import app
from app.models import Post, Page
from flask import render_template, url_for, send_from_directory


@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')


@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')


@app.route('/admin/post/list')
def admin_post_list():
    return render_template('admin/post_list.html')


@app.route('/admin/post/new')
def admin_post_new():
    return render_template('admin/post_new.html')


@app.route('/admin/post/<slug>/edit')
def admin_post_edit(slug):
    post = Post.objects.get_or_404(slug=slug)
    return render_template('admin/post_edit.html', post=post)
