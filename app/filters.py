from flask.ext.babel import format_datetime
from app import app

@app.template_filter('posted_at')
def posted_at(value):
    format = "dd/MM/y 'à' HH'h'mm"
    return format_datetime(value, format)

@app.template_filter('post_summary')
def post_summary(body):
    return body.partition('<!--more-->')[0]
