import os, sys

PROJECT_DIR = '/var/www/blog'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
exec(open(activate_this).read(), dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from app import app as application
