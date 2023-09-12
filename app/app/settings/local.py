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


# cloudinary setup configurations for media storages
USE_CLOUDINARY = os.environ.get('USE_CLOUDINARY')
if USE_CLOUDINARY=='True':
    INSTALLED_APPS += ['cloudinary','cloudinary_storage']
    # MEDIA_LOCATION = "media"
    # MEDIA_URL = f"https://res.cloudinary.com//"
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_SECRET_KEY'),
    }
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



# Email configuration
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_USE_SLS = os.environ.get('EMAIL_USE_SLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
APPLICATION_EMAIL = os.environ.get('APPLICATION_EMAIL')
DEFAULT_FROM_EMAIL=os.environ.get('DEFAULT_FROM_EMAIL')


# cache time interval
CACHE_TTL = 60 * 60 * 24

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}



# channel layer configurations
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}


CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"


REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT =os.environ.get("REDIS_PORT")
