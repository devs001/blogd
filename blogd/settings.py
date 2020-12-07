"""
Django settings for blogd project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib import messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import django_heroku

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@_1hzhu*j*c(9llt4=8wzw^-yklthsdd)o%r&2n_a6(5bca83!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_ID= 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'artical',
    'bootstrap4',
    'users',
    'taggit',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sitemaps',
    'tinymce',
    'channels'
    #'whitenoise.runserver_nostatic', # new!

    #'social_django',
    #'social.apps.django_app.default'
]
TINYMCE_DEFAULT_CONFIG={
    "theme": "silver",
    "height": 500,
    "menubar": True,
    "cleanup_on_startup":True,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor," 
               "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
               "code,help,wordcount",
    "toolbar": "undo redo | formatselect | fullscreen preview"
               "bold italic backcolor | alignleft aligncenter "
               "alignright alignjustify | bullist numlist outdent indent | "
               "removeformat | help",
    'statusbar':True,
    'file_browser_callback' : "myFileBrowser",
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'blogd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                #'social.apps.django_app.context_processors.backends',
                #'social.app.django_app.context_processors.login_redirects'
            ],
        },
    },
]

WSGI_APPLICATION = 'blogd.wsgi.application'
ASGI_APPLICATION= 'blogd.routing.application'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

MASSAGE_TAGS=[

]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL='users:login'

#<------ for sending mail ------>

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#SERVER_EMAIL= 'devendersandhu001@gmail.com'
EMAIL_HOST ='smtp.mailgun.org'
EMAIL_HOST_USER='postmaster@sandbox7e8dacc9aeac45a0a542262fdce95c87.mailgun.org'
EMAIL_HOST_PASSWORD='7b96cd194c107d0497136d88c6c089b7-2af183ba-2a688401'
EMAIL_PORT=587
EMAIL_USE_TLS=True

#<---- end of sending mail ----->

#<----- scoil-media auth system --->


AUTHENTICATION_BACKENDS =(
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',


    #'social.backends.facebook.FacebookOAuth2',
    #'social.backends.google.GoogleOAuth2',
    #'social.backends.twitter.TwitterOAuth',
    #'social.contrib.auth.backends.ModelsBackend'
)
SITE_ID=1
LOGIN_REDIRECT_URL='first'
LOGOUT_REDIRECT_URL='first'
LOGOUT_URL = 'first'

SOCIALACCOUNT_PROVIDERS={
    'google': {
    'SCOPE':['profile','email'],
    'AUTH_PARAMS':{
        'access_type':'online'
        }
    }
}

if os.getcwd() == '/app':
    import dj_database_url
    DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
    }

django_heroku.settings(locals())
