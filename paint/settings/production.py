"""
Settings for the Paint project

Production
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR + '/apps')

### Server Configuration ########################################### 

DEBUG = False
WSGI_APPLICATION = 'paint.wsgi.production.application'
ROOT_URLCONF = 'paint.urls'
ALLOWED_HOSTS = []
SECRET_KEY = 'changeme' # @TODO: should be changed in production


### Databse Configuration ###########################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}

### Middleware Configuration ###########################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

### Templates Configuration ###########################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

############################################################
# Applications 
############################################################


INSTALLED_APPS = [
    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # External
    'rest_framework',
    # Paint
    'paint.apps.authentication',
    'paint.apps.batch',
    'paint.apps.history'
]

### Batch ### 
THROTTLE_PERIOD_USER = os.environ.get('BATCH_THROTTLE_RANGE', 'day')
THROTTLE_COUNT_USER = int(os.environ.get('BATCH_THROTTLE_COUNT', '1000'))
THROTTLE_USER = f'{THROTTLE_COUNT_USER}/{THROTTLE_PERIOD_USER}'

THROTTLE_PERIOD_ANON = os.environ.get('BATCH_THROTTLE_RANGE', 'day')
THROTTLE_COUNT_ANON = int(os.environ.get('BATCH_THROTTLE_COUNT', '100'))
THROTTLE_ANON = f'{THROTTLE_COUNT_ANON}/{THROTTLE_PERIOD_ANON}'

### Django Rest Framework ###

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_THROTTLE_CLASSES': [
        'paint.util.throttle.AnonymousThrottle',
        'paint.util.throttle.UserThrottle'
    ]
}


### Authentication ###

AUTH_USER_MODEL = 'authentication.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

### Extra ###########################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
