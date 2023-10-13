
#from decouple import Config, Csv
from pathlib import Path
import os
import environ



#config = Config('.env')


env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
# Load environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.getenv("DEBUG")
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0",
                 "127.0.0.1", "moveritems.pythonanywhere.com"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mover',

    # third party apps
    'django_browser_reload',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files

# MEDIA_ROOT = [BASE_DIR, 'media']
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'mover.CustomUser'

# Django allauth


# https://django-jazzmin.readthedocs.io/configuration/

JAZZMIN_SETTINGS = {
    "site_title": "Mover Admin",
    "site_header": "Mover",
    "copyright": "Mover 2023",
    "site_brand": "Mover",
}

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = '/'



"""
# Email config

"""


"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'  # SMTP server for SendGrid
EMAIL_PORT = 587  # Port for SendGrid
EMAIL_USE_TLS = True  # Use TLS for secure connection

# Your SendGrid API key
SENDGRID_API_KEY = env('SENDGRID_API_KEY')

# Default sender for emails sent by your application
DEFAULT_FROM_EMAIL = 'your_email@example.com'
SERVER_EMAIL = 'your_email@example.com'

# Configure the SendGrid API client
sg = SendGridAPIClient(SENDGRID_API_KEY)
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'in-v3.mailjet.com'  # Mailjet SMTP server
EMAIL_PORT = 587  # TLS port
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '7061f15843b64b586576b4d3f10e80c4' #  env('API_KEY')  # Replace with your Mailjet API key
EMAIL_HOST_PASSWORD = 'da32aafbc47f8d9861e76e599bcb029c'  #  env('API_SECRET')  # Replace with your Mailjet API secret