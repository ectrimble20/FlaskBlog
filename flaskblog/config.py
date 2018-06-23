import os


class Config(object):
    ENV = os.environ.get('FLASK_BB_ENV', 'production')
    DEBUG = os.environ.get('FLASK_BB_DEBUG', False)
    TESTING = os.environ.get('FLASK_BB_TESTING', False)
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_DB_URI')
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FLASK_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('FLASK_EMAIL_PASS')
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
