from .base import *

SECRET_KEY = '!r&p!-29348io=o&h$u0n)%b!x%-3t17y$c!jor4bo*+ii0fex'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
