"""
Django settings for vmcexamplesite project.
"""

from django.core.management.utils import get_random_secret_key
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = get_random_secret_key()

DEBUG = 1

ALLOWED_HOSTS = "localhost"

INSTALLED_APPS = ["vertical_multi_columns"]

ROOT_URLCONF = "example_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "example_site/templates")],
    },
]

VERTICAL_MULTI_COLUMNS = [
    {"NUMBER_OF_COLUMNS": 3},
]
