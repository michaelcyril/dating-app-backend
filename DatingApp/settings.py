"""
Django settings for DatingApp project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from firebase_admin import initialize_app, credentials
from google.auth import load_credentials_from_file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*2kcc=%%ikue%ieqfdp)5v556&t@-p^_xzhgs2k-k8hk!g)qc&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Use UTF-8 as the default encoding
DEFAULT_CHARSET = 'UTF-8'

# Set the file system encoding
FILE_CHARSET = 'UTF-8'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'channels',
    "rest_framework",
    'user_management',
    'post_management',
    'social_management',
    'rest_framework.authtoken',
    'fcm_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DatingApp.urls'
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

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

WSGI_APPLICATION = 'DatingApp.wsgi.application'
ASGI_APPLICATION = 'DatingApp.routing.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # for normal authentication
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # jwt configgurations
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',

    ]
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'datingdb',
#     'USER': 'postgres',
#     'PASSWORD': '2024d@tingApp',
#     'HOST': '157.245.109.105',
#     'PORT': '5432',
#     'OPTIONS': {'sslmode': 'require','client_encoding': 'UTF8'},
#     'ATOMIC_REQUESTS': True,
#     'CHARSET': 'UTF-8',
#   }
# }

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'datingdb',
    'USER': 'postgres',
    # 'PASSWORD': '1234',
    'PASSWORD': 'Michael@71',
    'HOST': 'localhost',
    'PORT': '5432',
    'OPTIONS': {'client_encoding': 'UTF8'},
    'ATOMIC_REQUESTS': True,
    'CHARSET': 'UTF-8',
  }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


AUTH_USER_MODEL = 'user_management.User'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
DATA_UPLOAD_MAX_MEMORY_SIZE = 409600000

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

file_relative_path = "serviceAccountKey.json"
file_absolute_path = BASE_DIR / file_relative_path




class CustomFirebaseCredentials(credentials.ApplicationDefault):
    def __init__(self, account_file_path: str):
        super().__init__()
        self._account_file_path = account_file_path

    def _load_credential(self):
        if not self._g_credential:
            self._g_credential, self._project_id = load_credentials_from_file(self._account_file_path,
                                                                              scopes=credentials._scopes)
            
            

# 'CUSTOM_GOOGLE_APPLICATION_CREDENTIALS' ='f'
custom_credentials = CustomFirebaseCredentials(os.getenv('file_absolute_path'))
FIREBASE_MESSAGING_APP = initialize_app(custom_credentials, name='messaging')

FCM_DJANGO_SETTINGS = {
     # an instance of firebase_admin.App to be used as default for all fcm-django requests
     # default: None (the default Firebase app)
    "DEFAULT_FIREBASE_APP": FIREBASE_MESSAGING_APP,
     # default: _('FCM Django')
    "APP_VERBOSE_NAME": "What ever name",
     # true if you want to have only one active device per registered user at a time
     # default: False
    "ONE_DEVICE_PER_USER": False,
     # devices to which notifications cannot be sent,
     # are deleted upon receiving error response from FCM
     # default: False
    "DELETE_INACTIVE_DEVICES": False,
}