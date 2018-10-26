# Production Settings File

from .common import *

import dj_database_url


DEBUG=False
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

