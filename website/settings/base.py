import os
from decouple import config
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECRET_KEY = 'django-insecure-bb%m(m3qqipl&p+_^(bpv^(+grm3-+p77@7#la)oovxiu3w$3_'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'crispy_forms',
    'django_countries',
    'ckeditor',
    'tinymce',
    'embed_video',

    'blog',
    'video',
    'music',
    'marketing',
    'event',
    'emission',

    'taggit',
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # Corsheader
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('templates')],
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

WSGI_APPLICATION = 'website.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/


from django.utils.translation import gettext_lazy as _

LOCALE_PATH = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('fr', _('Francais')),
    ('en', _('Anglais')),
)


TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MAILCHIMP_API_KEY = ''
MAILCHIMP_DATA_CENTER = ''
MAILCHIMP_EMAIL_LIST_ID = ''

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'elfariid22@gmail.com'  # Enter your email
EMAIL_HOST_PASSWORD = 'pvgiqyscxyibmcav'  # Enter the password to the email
