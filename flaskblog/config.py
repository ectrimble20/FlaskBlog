import os


class Config(object):
    ENV = os.environ.get('FLASK_BB_ENV', 'production')
    DEBUG = os.environ.get('FLASK_BB_DEBUG', False)
    TESTING = os.environ.get('FLASK_BB_TESTING', False)
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_DB_URI')
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
