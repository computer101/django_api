import os
from pathlib import Path
from dotenv import load_dotenv

# ─────── Load .env (if it exists) ───────
env_path = Path(__file__).resolve().parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# ─────── BASE DIR ─────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─────── SECURITY & DEBUG ─────────────
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "yes")
ALLOWED_HOSTS = []

# ─────── INSTALLED APPS ────────────────
INSTALLED_APPS = [
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # django-allauth + dependencies
    "django.contrib.sites",                  # ← required by allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",

    # Our app
    "app",
]

# ─────── MIDDLEWARE ────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    # Django’s authentication middleware must come before AllAuth’s:
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Add AllAuth’s AccountMiddleware:
    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ─────── URL CONFIGURATION ─────────────
ROOT_URLCONF = "Ywork.urls"

# ─────── TEMPLATES ────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # ← required by allauth
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ─────── WSGI APPLICATION ─────────────
WSGI_APPLICATION = "Ywork.wsgi.application"

# ─────── DATABASES ─────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ─────── PASSWORD VALIDATORS ───────────
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ─────── INTERNATIONALIZATION ───────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ─────── STATIC FILES ──────────────────
STATIC_URL = "/static/"

# ─────── django-allauth SETTINGS ───────
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",            # default
    "allauth.account.auth_backends.AuthenticationBackend",  # allauth
]

# Redirect after login/signup
ACCOUNT_LOGIN_REDIRECT_URL = "/profile/"
# Redirect after logout
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

# ─── Replace deprecated settings with the new ones ────────────────────────────

# Allow login by username OR email:
ACCOUNT_LOGIN_METHODS = {"username", "email"}

# Specify the fields to collect at signup (email is required, indicated by the asterisk):
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]

# Disable email verification for simplicity (optional):
ACCOUNT_EMAIL_VERIFICATION = "none"

# ─────── Google OAuth2 configuration ─────────────
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
            "openid",
        ],
        # Request offline access to receive a refresh token:
        "AUTH_PARAMS": {
            "access_type": "offline",
            "prompt": "consent",
        },
        "APP": {
            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
            "secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
            "key": "",
        },
    }
}
