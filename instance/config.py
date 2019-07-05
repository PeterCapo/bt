import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


class ReleaseConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
    'db_url': "postgres://qhxwbysu:Ly5l-uZICzJ-G-Z0SmVasYLsy_wtqpPa@raja.db.elephantsql.com:5432/qhxwbysu"
}