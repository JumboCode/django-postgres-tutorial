#
# These are settings for local development
#

from .common import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

ALLOWED_HOSTS = ['localhost']
SECRET_KEY = 'm&%ij7#cpxk$p2w(@%u#7s)_$@!%)#fgp&^7q&0id1b4(fg(o&'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'switch_dev',
        'USER': 'dev',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}