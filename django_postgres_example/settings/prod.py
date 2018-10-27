#
# These are settings for Heroku Production Environment
#

from .common import *

import dj_database_url


DEBUG=False
SECURE_SSL_REDIRECT = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ["jcdjangopostgres.herokuapp.com"]

DATABASES = { }

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

