#
#   These are the settings for a Travis Integrating Testing Environments
#

from .common import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

ALLOWED_HOSTS = ['localhost']
SECRET_KEY = 'm&%ij7#cpxk$p2w(@%u#7s)_$@!%)#fgp&^7q&0id1b4(fg(o&'
STATIC_URL = '/static/'

DEBUG = True

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
