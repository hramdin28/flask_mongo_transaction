import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    MONGODB_SETTINGS = [
        {
            'alias': 'default',
            'db': 'test_db',
            'host': 'mongo1',
            'port': 27017,
            'username': 'root',
            'password': 'rootpassword'
        },
        {
            'alias': 'mongo2',
            'db': 'test_db',
            'host': 'mongo2',
            'port': 27018,
            'username': 'root',
            'password': 'rootpassword'
        },
        {
            'alias': 'mongo3',
            'db': 'test_db',
            'host': 'mongo1',
            'port': 27019,
            'username': 'root',
            'password': 'rootpassword'
        }
    ]


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'test_db',
        'host': 'localhost',
        'port': 27017,
        'username': 'root',
        'password': 'rootpassword'
    }


config_by_profile = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
