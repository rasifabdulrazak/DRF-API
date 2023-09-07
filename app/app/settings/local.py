from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

# only configure needed hosts
ALLOWED_HOSTS = ['*']

# timzone may be diffrent according to projects
TIME_ZONE = os.environ.get('TIME_ZONE')

# static and media roots configurations
# Static files (CSS, JavaScript, Images) -> docker path
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/pub/static/'
MEDIA_URL = "/pub/media/"
MEDIA_ROOT = "/vol/web/media/"
STATIC_ROOT = "/vol/web/static/"


# logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "/log/error.log",
            "formatter":"simple"
        },
        "critical_file": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "filename": "/log/critical.log",
            "formatter":"simple"
        },
    },
    "loggers": {
        "error_log": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": True,
        },
        "critical_log": {
            "handlers": ["critical_file"],
            "level": "CRITICAL",
            "propagate": True,
        },
    },
    "formatters": {
        "simple": {
            "format": "{asctime} {levelname} {module} {message}",
            "style": "{",
        }
    },

}


# swagger ui api documentation setup configuration
SPECTACULAR_SETTINGS = {
    'TITLE': 'DRF-API',
    'DESCRIPTION': 'API documentation for my DRF-API',
    'VERSION': '1.0.0',
    'SWAGGER_UI_SETTINGS': {
        'docExpansion': 'list',
        'filter': True,
        'persistAuthorization': True,
    },
}


# Debug toolbar configuration -> for query testing and optimisations
if DEBUG=='True':
    INSTALLED_APPS += ['debug_toolbar',]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: not request.is_ajax()
    }


# Database backup configuration -> currently saving in server itself, update in production
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.environ.get('DB_BACKUP_LOCATION')}


