from pathlib import Path
import os


import os
from pathlib import Path

# 기본 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 정적 파일 설정
STATIC_URL = '/static/'
# 정적 파일을 서빙할 루트 디렉토리 설정 (optional)
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# 정적 파일 디렉토리 설정
STATICFILES_DIRS = [
    BASE_DIR / 'navigation' / 'static',  # 상대 경로
    'C:/Users/김수빈/safety_route/navigation/static',  # 절대 경로
]



# 보안 헤더 추가
SECURE_CONTENT_TYPE_NOSNIFF = True

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-l-%z65bhwve1-uclyh$m26!t6+d!)nbx%*hb%mna4qd%i-ua^3'
DEBUG = False
ALLOWED_HOSTS = ['.pythonanywhere.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'navigation',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'safety_route.urls'

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

WSGI_APPLICATION = 'safety_route.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
