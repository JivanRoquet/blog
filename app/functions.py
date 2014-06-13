from app import app
from app.models import Page, Post
from collections import defaultdict
import operator


def get_menu_pages():
    pages = Page.objects(in_top_menu=True, published=True).only("url", "label")
    return pages


def get_sidebar_tags():
    posts = Post.objects(published=True).only("tags")
    tags = defaultdict(int)
    for post in posts:
        for tag in post.tags:
            tags[tag] += 1
    return sorted(tags.items(), key=operator.itemgetter(1), reverse=True)

app.jinja_env.globals.update(get_menu_pages=get_menu_pages)
app.jinja_env.globals.update(get_sidebar_tags=get_sidebar_tags)
