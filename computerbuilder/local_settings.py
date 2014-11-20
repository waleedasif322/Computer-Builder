"""
Django settings for computerbuilder project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zd-p&nwm28bm+p#tsfpxq)lxq@r$yzzf-j_xohh$r6i4ms*g%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.sites',
    'registration',
    'django.contrib.humanize',
    'builds',
    'parts',
    'south',
    'ajax_select',
    'userprofile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'computerbuilder.urls'

WSGI_APPLICATION = 'computerbuilder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Parse database configuration from $DATABASE_URL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compdb',
	'USER': 'admincp',
	'PASSWORD': 'computerbuilder',
	'HOST': 'localhost',
	'PORT':'',

    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

import dj_database_url

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(os.path.dirname(__file__),'static').replace('\\','/'),
)

STATIC_ROOT = "/"

TEMPLATE_DIRS = (
  os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),
)




#Let us set up the mail settings and the activation days for registration
#Here we are setting it up for testing purposes
ACCOUNT_ACTIVATION_DAYS=7

EMAIL_HOST='localhost'
EMAIL_PORT=1025
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@foxacid.com'


#Some settings for the captcha
RECAPTCHA_PUBLIC_KEY = '76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh'
RECAPTCHA_PRIVATE_KEY = '98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs'
RECAPTCHA_USE_SSL = True


# define the lookup channels in use on the site
AJAX_LOOKUP_CHANNELS = {
    #simple: search Person.objects.filter(name__icontains=q)
    #'person'  : {'model': 'example.person', 'search_field': 'name'},
    # define a custom lookup channel
    #'song'   : ('example.lookups', 'SongLookup')
    #'moboListing' : {'model': 'parts.moboListing', 'search_field': 'moboList'},
    'moboListing': ('builds.lookups', 'moboLookup'),
    'cpuListing': ('builds.lookups', 'cpuLookup'),
    'gpuListing': ('builds.lookups', 'gpuLookup'),
    'memListing': ('builds.lookups', 'memLookup'),
    'hdListing': ('builds.lookups', 'hdLookup'),
    'caseListing': ('builds.lookups', 'caseLookup'),    
}

AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'

#userprofiles
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

SITE_ID = 1

