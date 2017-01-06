"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from django.core.exceptions import ImproperlyConfigured


print("system=->", sys.path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    print(os.environ[var_name])
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable.".format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable('DJANGO_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ['127.0.0.1', '::1']

ALLOWED_HOSTS = ['*', ]

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'snowpenguin.django.recaptcha2',
    'bootstrap3',
    'django_countries',
    'rules_light',
    'mptt',
    'pagination_bootstrap',
    'askapp',
)

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'rules_light.middleware.Middleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'askapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(BASE_DIR) + '/askapp/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'askapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# [START db_setup]
# get database parameters from environment variables
DB_HOST = get_env_variable('DB_HOST')
DB_DATABASE = get_env_variable('DB_DATABASE')
DB_USER = get_env_variable('DB_USER')
DB_PASSWORD = get_env_variable('DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
    }

}
# [END db_setup]

# [django-registration] related parameters
# https://django-registration.readthedocs.io/en/2.2/
ACCOUNT_ACTIVATION_DAYS = 7
# [END django-registration]

EMAIL = get_env_variable('EMAIL_ADDRESS')

# outgoing mail server settings
SERVER_EMAIL = EMAIL
DEFAULT_FROM_EMAIL = EMAIL
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT_PREFIX = '[Akihabara.Tokyo]'
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC_ROOT='static'
STATIC_ROOT = os.path.join(BASE_DIR, "askapp/static")

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'auth.User'

#the url where the user will be redirected after they log in
LOGIN_REDIRECT_URL = '/'

#RECAPTCHA KEYS
RECAPTCHA_PRIVATE_KEY = get_env_variable('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PUBLIC_KEY = get_env_variable('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PROXY = 'http://127.0.0.1:8000'

BLACKLISTED_DOMAINS = ['yopmail1.com', ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'askapp/media')

AVATAR_SIZE = (100, 100)

PAGINATION_DEFAULT_PAGINATION = 10