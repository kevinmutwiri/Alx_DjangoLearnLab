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
    'csp', # Required for Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware', # Add CSP middleware for Content Security Policy
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

# --- HTTPS and Security Settings ---

# SECURE_SSL_REDIRECT: Redirects all non-HTTPS requests to HTTPS.
# This should be True in production. Ensure your web server (e.g., Nginx, Apache)
# is configured to serve HTTPS before enabling this.
SECURE_SSL_REDIRECT = True

# SECURE_HSTS_SECONDS: Enables HTTP Strict Transport Security (HSTS).
# Forces browsers to interact with your site only over HTTPS for the specified duration (in seconds).
# Set to a large value (e.g., 31536000 for 1 year) in production.
SECURE_HSTS_SECONDS = 31536000

# SECURE_HSTS_INCLUDE_SUBDOMAINS: Includes all subdomains in the HSTS policy.
# Recommended to be True in production if all subdomains also support HTTPS.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_HSTS_PRELOAD: Allows your domain to be preloaded into browsers' HSTS lists.
# Only set to True after successfully deploying HSTS and meeting preload requirements.
SECURE_HSTS_PRELOAD = True

# SESSION_COOKIE_SECURE: Ensures that session cookies are only transmitted over HTTPS.
# Prevents session hijacking over insecure connections.
SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE: Ensures that CSRF cookies are only transmitted over HTTPS.
# Protects against CSRF token leakage over insecure connections.
CSRF_COOKIE_SECURE = True

# X_FRAME_OPTIONS: Prevents your site from being embedded in a frame on another site.
# Protects against clickjacking attacks. 'DENY' is the most secure option.
X_FRAME_OPTIONS = 'DENY'

# SECURE_CONTENT_TYPE_NOSNIFF: Prevents browsers from MIME-sniffing a response.
# Helps prevent XSS attacks by ensuring browsers respect the Content-Type header.
SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_BROWSER_XSS_FILTER: Enables the browser's built-in XSS filter.
# Provides an additional layer of defense against XSS attacks.
SECURE_BROWSER_XSS_FILTER = True

# Content Security Policy (CSP) configuration using django-csp
# This is a robust defense against XSS. Customize these directives based on your application's needs.
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
