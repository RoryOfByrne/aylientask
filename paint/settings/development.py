"""
Settings for the Paint project

Development
"""

from paint.settings.production import *

### Server Configuration ###########################################

DEBUG = True
WSGI_APPLICATION = 'paint.wsgi.development.application'
ALLOWED_HOSTS = ['localhost']
SECRET_KEY = 'abc' # @TODO: should be changed in production

### Databse Configuration ###########################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}