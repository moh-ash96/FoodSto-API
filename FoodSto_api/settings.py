from pathlib import Path
import environ
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "PRODUCTION"),
    ALLOW_ALL_ORIGINS=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ALLOWED_ORIGINS=(list, []),
    DATABASE_ENGINE=(str, "django.db.backends.sqlite3"),
    DATABASE_NAME=(str, BASE_DIR / "db.sqlite3"),
    DATABASE_USER=(str, ""),
    DATABASE_PASSWORD=(str, ""),
    DATABASE_HOST=(str, ""),
    DATABASE_PORT=(int, 5432),
)

environ.Env.read_env()

ENVIRONMENT = env.str("ENVIRONMENT")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS"))


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "rest_framework",
    "corsheaders",
    # local
    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "FoodSto_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "FoodSto_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.int("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# AUTH_USER_MODEL = "accounts.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

CORS_ORIGIN_WHITELIST = tuple(env.list("ALLOWED_ORIGINS"))
CORS_ALLOW_ALL_ORIGINS = env.bool("ALLOW_ALL_ORIGINS")

# Activate Django-Heroku.
django_heroku.settings(locals())