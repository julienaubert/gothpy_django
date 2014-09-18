import os
from .base import GOTHPY_DJANGO_EX_LOG_DIR

if not os.path.exists(GOTHPY_DJANGO_EX_LOG_DIR):
    os.makedirs(GOTHPY_DJANGO_EX_LOG_DIR)


def file_handler(name, level):
    return {
        'level': level,
        'class': 'logging.handlers.RotatingFileHandler',
        'formatter': 'full',
        'filename': os.path.join(GOTHPY_DJANGO_EX_LOG_DIR, '{}.log'.format(name)),
    }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'full': {
            'format': '%(levelname)-8s: %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'verbose': {
            'format': '%(levelname)-8s: %(asctime)s %(name)20s %(message)s'
        },
        'simple': {
            'format': '%(levelname)-8s: %(asctime)s %(name)20s: %(funcName)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler'
        },
        'errors': file_handler('errors', 'DEBUG'),
        'security': file_handler('security', 'DEBUG'),
        'business': file_handler('business', 'DEBUG'),
        'root': file_handler('messages', 'DEBUG'),
        'application': file_handler('gothpy_django_ex', 'DEBUG'),
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['root'],
            'propagate': True,
            'level': 'ERROR'
        },
        'django.request': {
            'handlers': ['root'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.db.backends': {
            'handlers': ['root'],
            'level': 'ERROR',
            'propagate': True
        },
        'errors': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': True
        },
        'exceptions': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': True
        },
        'security': {
            'handlers': ['security'],
            'level': 'INFO',
            'propagate': False
        },
        'testing': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'gothpy_django_ex': {
            'handlers': ['application'],
            'level': 'ERROR',
            'propagate': True
        },
        'gothpy_django_ex.settings': {
            'handlers': ['application'],
            'level': 'ERROR',
            'propagate': True
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

LOGGING_DEBUG = {
    'version': 1,
    'disable_existing_loggers': True,
}
