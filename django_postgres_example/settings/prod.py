#
# These are settings for Heroku Production Environment
#

from .common import *

import dj_database_url


# We don't want any debug warnings giving
# away unnecessary information to attackers

DEBUG=False

# We grab the secret key from the environment because it is
# our production key and no can know it

SECRET_KEY = os.environ.get('SECRET_KEY')

# We redirect any http requests to their  https equivalents

SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ["jcdjangopostgres.herokuapp.com"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# In a real production environment, we would likely want to
# handle static files on a different machine.

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# We let the dj_database_url package pull the database info from heroku
# https://github.com/kennethreitz/dj-database-url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
