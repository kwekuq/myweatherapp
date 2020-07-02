from .base import *

SECRET_KEY = 'O*)UIU(&T7u34rih;fnwe08yu32edwert4ge43tfgvrtj65'
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

OPENWEATHERMAP_API = '889a55666a1b2dee775d135241b7d416'
