# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get("SECRET_KEY", "something")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
S3DIRECT_REGION = os.environ.get("AWS_REGION")
AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET")
DATABASE_URL = os.environ.get("DATABASE_URL")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    's3direct',
    'common',
    'photo',
    'registry',
    'rsvp',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'common.renderers.SiteJsonRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    'templates',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


S3DIRECT_DESTINATIONS = {
    # Allow anybody to upload jpeg's and png's.
    'imgs': ('img', lambda u: True, ['image/jpeg', 'image/png'],),

    # Allow logged in users to upload any type of file and give it a private acl:
    'private': (
        'uploads/vids',
        lambda u: u.is_authenticated(),
        '*',
        'private'),

    # Allow authenticated users to upload with cache-control for a month and
    # content-disposition set to attachment
    'cached': (
        'uploads/vids',
        lambda u: u.is_authenticated(),
        '*',
        'public-read',
        AWS_STORAGE_BUCKET_NAME,
        'max-age=2592000',
        'attachment')
}
