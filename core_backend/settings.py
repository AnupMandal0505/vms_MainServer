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
import dj_database_url

from dotenv import load_dotenv
load_dotenv()  # Load the environment variables from the .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('SECRET_KEY',)
SECRET_KEY='django-insecure-$19ohzt@k1k!q7r0qs2!p1=p0a=hnzg2m)@u8l&pths=#7!mll'
# Optional: Set DEBUG dynamically
DEBUG = os.getenv('DEBUG', 'False')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['vms-mainserver.onrender.com']
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# ALLOWED_HOSTS = ['servicebasedauthentication.onrender.com', '127.0.0.1', 'localhost',"192.168.4.224"]

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
    "corsheaders.middleware.CorsMiddleware",  #  Add this at the top
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


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
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

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# STATIC_URL = "/static/"

# # If using local static files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# # If collecting static files for deployment
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = '/static/'

# Define the location of static files for development
STATIC_ROOT =  BASE_DIR / "staticfiles"


# Whitenoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = BASE_DIR





# Email Section................
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'



# Allow all origins
CORS_ALLOW_ALL_ORIGINS = True

# Restrict allowed methods
CORS_ALLOW_METHODS = [
    "GET",  # ✅ Allow only safe methods like GET
    "OPTIONS",
]

# Allow all headers (needed for security tokens, etc.)
CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
]
CSRF_TRUSTED_ORIGINS='https://vms-mainserver.onrender.com'


# CORS_ALLOW_ALL_ORIGINS = False
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://.*\.yourdomain\.com$",  # ✅ Allow all subdomains of yourdomain.com
#     r"^https://your-client-.*\.com$",  # ✅ Example: Allow dynamic client domains
# ]
