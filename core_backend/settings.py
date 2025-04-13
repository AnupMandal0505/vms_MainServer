"""
Django settings for core_backend project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
# import dj_database_url

from dotenv import load_dotenv
load_dotenv()  # Load the environment variables from the .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback_secret")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS = ['vms-mainserver.onrender.com','127.0.0.1','192.168.54.224',]
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
ALLOWED_HOSTS = ['casemfc.com','194.164.149.231','172.22.226.236','127.0.0.1','localhost']

DOMAIN_NAME = os.getenv("API_BASE_URL")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'home_server',
    'technical',
    'client',
    'apis',
    'whitenoise',
    'corsheaders',

]

AUTH_USER_MODEL = "home_server.ClientUser"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  #  Add this at the top
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core_backend.urls'

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

WSGI_APPLICATION = 'core_backend.wsgi.application'



# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/dbname"))
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'your_db_name'),
        'USER': os.getenv('POSTGRES_USER', 'your_db_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'your_db_password'),
        'HOST': os.getenv('DB_HOST', 'db'),  # "db" Docker Compose service ka naam hai
        'PORT': os.getenv('DB_PORT', '5432'),  # PostgreSQL ka default port
    }
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    }
}


# Celery
CELERY_BROKER_URL = os.environ.get(
    'RABBITMQ_URL', 'amqp://guest:guest@msgbroker:5672//'
)


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email Section................
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'





# Add CSRF protection
# CSRF_TRUSTED_ORIGINS = ['https://vms.casesmfc.com']

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# CORS_ALLOWED_ORIGINS = ['https://vms.casesmfc.com','https://admin.vms.casesmfc.com']

# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )

# CORS_ALLOW_CREDENTIALS = True


ADMIN_SITE_HEADER = 'Appointment Server Admin'
ADMIN_SITE_TITLE = 'Appointment Server'



# Add this to your settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}