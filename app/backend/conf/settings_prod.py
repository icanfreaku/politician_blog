from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'HOST': 'db',
        'PORT': 5432,
    }
}

ALLOWED_HOSTS = ['*']
STATICFILES_DIRS = ()
STATIC_ROOT = '/static/'

DEBUG = False
TEMPLATE_DEBUG = False

# UNCOMMENT BELOW IF USING SSL
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'applogfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/logs/app/app.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['applogfile'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}