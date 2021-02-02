"""
Django settings for vmcexamplesite project.
"""

from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = <insert your Django secret key here>

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
    },
]

VERTICAL_MULTI_COLUMNS = [
    {'NUMBER_OF_COLUMNS': 3},
]