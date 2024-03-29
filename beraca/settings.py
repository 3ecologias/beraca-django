"""
Django settings for beraca project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g8!s)#%ww*y2gjd%63dv43y3&@s7f4gf+80l%_&*cr)g=$$pdt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['www.institutoberaca.org', 'institutoberaca.org']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'core',
    'ckeditor',
    'maintenance_mode',

    'robots'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'beraca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'beraca.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
 }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'beracawebsite',
#         'USER': 'beraca',
#         'PASSWORD': 'Tatub0la',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# CACHE settings
CACHE_MIDDLEWARE_ALIAS = "cache_ib"
CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_KEY_PREFIX = "IB"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_ib',
        'TIMEOUT': 300,
        'OPTIONS': {'MAX_ENTRIES': 300}
    },
    'cache_ib': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_ib',
        'TIMEOUT': 300,
        'OPTIONS': {'MAX_ENTRIES': 300}
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


##CK EDITOR CONFIGS ##

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}

##EMAIL CONFIGS
# Console [test purposes]
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

##EMAIL CONFIGURATION
EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = "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"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'contato@institutoberaca.org'
# EMAIL_TO = 'contato@institutoberaca.org'
EMAIL_TO = 'lucazartu@gmail.com'
EMAIL_HOST_USER = '3ecologias'
EMAIL_HOST_PASSWORD = 'm1c0leao'
EMAIL_USE_TLS = True

## MODO DE MANUTENCAO
MAINTENANCE_MODE = False
MAINTENANCE_MODE_TEMPLATE = 'core/maintenance.html'
MAINTENANCE_MODE_IGNORE_SUPERUSER = True

## Captcha

GOOGLE_RECAPTCHA_SECRET_KEY = '6LdO5iQUAAAAAFukEi4HkdCtgskVEmzgjABwD16N'
