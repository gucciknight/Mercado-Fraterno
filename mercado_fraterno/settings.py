"""
Django settings for mercado_fraterno project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os

from pathlib import Path

import sys


# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c!-yz@0j3#m$@y&tkf41%e_r71t#k#x0-3rdyspk418fa6zij3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dev.tumonedasocial.com']


# Application definition

DJANGO_APPS = (
	'django.contrib.admin', 
	'django.contrib.auth', 
	'django.contrib.contenttypes', 
	'django.contrib.sessions', 
	'django.contrib.messages', 
	'django.contrib.staticfiles', 
    'django.contrib.humanize',
) 
THIRD_APPS = ( 
	#apps descargadas
    'django_extensions',
    'crispy_forms',
    'crispy_bootstrap4',
			  ) 
LOCAL_APPS = (
	#apps agregadas
    'core.apps.CoreConfig', 
			  ) 

INSTALLED_APPS = THIRD_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mercado_fraterno.urls'

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

WSGI_APPLICATION = 'mercado_fraterno.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3dev'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
'''
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
'''

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom Django auth settings

AUTH_USER_MODEL = 'core.User'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

ACCOUNT_USERNAME_REQUIRED = False    # This removes the username field

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'

EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp-relay.brevo.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'arodriguezluna93@gmail.com'

EMAIL_HOST_PASSWORD = 'VU9OGa6hjym73rWg'

DEFAULT_FROM_EMAIL = 'arodriguezluna93@gmail.com'
