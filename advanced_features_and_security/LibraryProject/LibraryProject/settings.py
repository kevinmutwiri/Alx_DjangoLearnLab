import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# This should be a long, random string. NEVER commit your actual production key to version control.
SECRET_KEY = 'django-insecure-your-secret-key-please-change-this-in-production!'

# SECURITY WARNING: don't run with debug turned on in production!
# Set to False for production environments.
DEBUG = False # Set to False for production

# ALLOWED_HOSTS: List of strings representing the host/domain names that this Django site can serve.
# In production, this should be set to your actual domain names (e.g., ['yourdomain.com', 'www.yourdomain.com']).
ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] # Example for development/testing, change for production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'csp', # Add django-csp for Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware', # Add CSP middleware
]

ROOT_URLCONF = 'advanced_features_and_security.urls'

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

WSGI_APPLICATION = 'advanced_features_and_security.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

AUTH_USER_MODEL = 'bookshelf.CustomUser'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security Settings Enhancements:

# Enforce that cookies are sent over HTTPS only.
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Prevent browsers from performing MIME sniffing.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Prevent pages from being embedded in iframes on other sites, protecting against clickjacking.
X_FRAME_OPTIONS = 'DENY'

# Enable browser's XSS filter.
SECURE_BROWSER_XSS_FILTER = True

# Redirect all non-HTTPS requests to HTTPS. Requires your server to handle HTTPS.
# SECURE_SSL_REDIRECT = True # Uncomment in production after setting up HTTPS

# Enable HTTP Strict Transport Security (HSTS). Forces browsers to only interact with your site over HTTPS.
# SECURE_HSTS_SECONDS = 31536000 # 1 year in seconds; uncomment in production after testing HTTPS
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Uncomment in production
# SECURE_HSTS_PRELOAD = True # Uncomment in production

# Content Security Policy (CSP) configuration using django-csp
# This is a basic example. You should customize these directives based on your application's needs.
# For more complex policies, consider using a more granular approach.
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net") # Example: allow inline scripts and CDN
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net") # Example: allow inline styles and CDN
CSP_IMG_SRC = ("'self'", "data:") # Allow images from self and data URIs
CSP_FONT_SRC = ("'self'", "data:") # Allow fonts from self and data URIs
CSP_CONNECT_SRC = ("'self'",)
CSP_FRAME_ANCESTORS = ("'self'",)
CSP_OBJECT_SRC = ("'none'",) # Disallow plugins like Flash
CSP_BASE_URI = ("'self'",)
CSP_FORM_ACTION = ("'self'",)
