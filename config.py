import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'jD9jqd<W@08*pNH('

DB = {
    'name': 'blog',
    'username': 'jivan',
    'password': 'mikmAc12.',
    'host': 'ds031359.mongolab.com:31359/blog'
}

MONGODB_DB = DB['name']
