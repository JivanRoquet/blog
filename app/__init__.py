from flask import Flask
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine
from flask.ext.babel import Babel
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# loads configuration
app.config.from_object('config')
app.debug = True

toolbar = DebugToolbarExtension(app)

babel = Babel(app)

# handles connection with MongoDB server
_db = app.config['DB']
_db_identifier = 'mongodb://{}:{}@{}'.format(_db['username'], _db['password'], _db['host'])
connect(_db['name'], host=_db_identifier)
db = MongoEngine(app)

from app import blog, models, filters, functions, admin
