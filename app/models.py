import datetime
from flask import url_for
from app import db


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    tags = db.ListField(db.StringField(max_length=30))
    published = db.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class Page(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    label = db.StringField(max_length=30, required=True)
    url = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    weight = db.IntField(default=0)
    in_top_menu = db.BooleanField(default=False)
    published = db.BooleanField(default=False)
    text = db.DateTimeField(default=datetime.datetime.now, required=True)

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['url', '-weight'],
        'ordering': ['-weight']
    }
