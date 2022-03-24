

import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-rx8bm1hi_^n!_a_5&bjkx0p0du$x(a6ws7_46sk$zx@j8z7w+6'


# DEBUG = True

# ALLOWED_HOSTS = ['*']


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',
    'category.apps.CategoryConfig',
    'tag.apps.TagConfig',
    'contact',
    'dashboard.apps.DashboardConfig',
    'accounts.apps.AccountsConfig',
    'rest_framework',
    'widget_tweaks',
    'social_django',
    'users', 
    'debug_toolbar',
    'ckeditor',
    'django.contrib.sitemaps',
    
    'rest_framework.authtoken',
    'dj_rest_auth',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'django_filters',
    
    'search.apps.SearchConfig',
    'django_elasticsearch_dsl',

    'location',
 
    ]

    
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'insurance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'insurance.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'api.permissions.IsStaffOrReadOnly',
    ],
      'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'access'
JWT_AUTH_REFRESH_COOKIE = 'refresh'

REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'api.serializers.RegisterSerializer',
}



DATABASES = {

     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insurance',
        'USER': 'postgres',
        'PASSWORD': 'siyamak1981',
        'HOST': 'db',
        'PORT': '5432',
    },
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'accounts.User'


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




LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'upload')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media', 'static'),
)


EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'siyamak1981@gmail.com'
EMAIL_HOST_PASSWORD = '****************'
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)


INTERNAL_IPS = [
    "127.0.0.1",
    'localhost'
]

DEBUG_TOOLBAR_CONFIG = {
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'my_cache_table',
   }
}

RECAPTCHA_PUBLIC_KEY = config("RECAPTCHA_PUBLIC_KEY",default="")
RECAPTCHA_PRIVATE_KEY = config("RECAPTCHA_PRIVATE_KEY",default="")

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '549418161873-vunmslj02haoovb8r9imscaoa2kad4sc.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' # Google Consumer Secret
SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_REDIRECT_URL = "dashboard:home"  
LOGOUT_REDIRECT_URL = 'login'



# CELERY STUFF
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': os.getenv("ELASTICSEARCH_DSL_HOSTS", 'localhost:9200')
    },
}

# GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
# GOOGLE_MAPS_API_KEY=AIzaSyAosgxc63Vzg0rPPulpvVrcl7NgQPX41UM