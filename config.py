# config.py
class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///example.db'
class DevelopmentConfig(Config):
    DEBUG = True
class TestingConfig(Config):
    TESTING = True

