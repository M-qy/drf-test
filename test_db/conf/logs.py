LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'log': {
            'format': '{asctime} - {levelname} - {message}',
            'style': '{',
        },
        'sql': {
            'format': '[{process}-{levelname}] [{asctime}] [{name}:{lineno}] - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'log',
            'level': 'INFO'
        },
        'log': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': 'logs/log',
            'formatter': 'log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 128,
            'backupCount': 5,
            'level': 'DEBUG'
        },
        'sql_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
            'level': 'DEBUG'
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['sql_console'],
            'level': 'DEBUG',
        },
        'test_log': {
            'handlers': ['console', 'log'],
            'level': 'DEBUG'
        }
    },
}
