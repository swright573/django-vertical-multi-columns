"""
Django settings for vmcexamplesite project.
"""

from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'we^d+w+iixgys4ds8^ap08rqgby9(uo-rufx(aod)$udk*!q!@'      #<your secret key>
DEBUG = 1
ALLOWED_HOSTS = 'localhost'
INSTALLED_APPS = [
    'vertical_multi_columns'
]
ROOT_URLCONF = 'vmcexamplesite.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'vmcexamplesite/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
               # 'django.template.context_processors.media'
            ],
        },
    },
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR + '/static/', )

VERTICAL_MULTI_COLUMNS = [
    {'NUMBER_OF_COLUMNS': 3}
]