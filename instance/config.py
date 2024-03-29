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
    'db_url': "postgres://dgiapvopgroeuf:93151de33e943a50c349133bb68e4bfd03a845fba756c0df9b3cba8ff9eae7f2@ec2-174-129-227-205.compute-1.amazonaws.com:5432/da8hv9kjap657g"
}