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
        },
        'info': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': 'logs/info',
            'formatter': 'log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 128,
            'backupCount': 5
        },
        'warn': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': 'logs/warn',
            'formatter': 'log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 128,
            'backupCount': 5
        },
        'error': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': 'logs/error',
            'formatter': 'log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 128,
            'backupCount': 5
        },
        'sql': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': 'logs/sql',
            'formatter': 'sql',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024 * 128,
            'backupCount': 5
        },
    },
    'loggers': {
        # 'django.db.backends': {
        #     'handlers': ['console', 'sql'],
        #     'level': 'DEBUG',
        # },
        # 'test.info': {
        #     'handlers': ['info'],
        #     'level': 'INFO',
        # },
        # 'test.warn': {
        #     'handlers': ['console', 'warn'],
        #     'level': 'WARNING',
        # },
        # 'test.error': {
        #     'handlers': ['console', 'error'],
        #     'level': 'ERROR',
        # },
    },
}
