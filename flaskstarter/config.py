# -*- coding: utf-8 -*-

import os

from .utils import INSTANCE_FOLDER_PATH


class BaseConfig(object):
    # Change these settings as per your needs

    PROJECT = "flaskstarter"
    PROJECT_NAME = "flaskstarter.domain"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    BASE_URL = "https://yourdomain-flaskstarter.domain"
    ADMIN_EMAILS = ['admin@flaskstarter.domain']

    DEBUG = False
    TESTING = False

    SECRET_KEY = 'always-change-this-secret-key-with-random-alpha-nums'


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-Sqlalchemy
    SQLALCHEMY_ECHO = True   # False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLITE for production
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/db.sqlite'
    DB_FILE = os.path.join(INSTANCE_FOLDER_PATH, 'db.sqlite')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'

    # POSTGRESQL for production
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:pass@ip/dbname'

    # Flask-cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail
    MAIL_DEBUG = True  # False
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '0237fa7e26adbe'
    MAIL_PASSWORD = '********4650'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'noreply@yourdomain.com'

    # Keep these in instance folder or in env variables
    MAIL_USERNAME = "Stratasyslab@gmail.com"
    MAIL_PASSWORD = "urcshsgdiwlainsu"  # Use App Password, not regular password
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
