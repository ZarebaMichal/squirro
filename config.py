from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    """Common configurations"""

    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    DEBUG = environ.get("DEBUG")
    TESTING = environ.get("TESTING")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")


class ProductionConfig(Config):
    """Production configurations"""

    DEBUG = environ.get("DEBUG")
    TESTING = environ.get("TESTING")
    FLASK_ENV = environ.get("FLASK_ENV")
