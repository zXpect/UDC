import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_URI = os.environ.get('MONGODB_URI')
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
    SESSION_TYPE = 'filesystem'  
    SESSION_PERMANENT = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # En producción, estas variables DEBEN estar definidas como variables de entorno
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_URI = os.environ.get('MONGODB_URI')
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

class TestingConfig(Config):
    TESTING = True
    MONGODB_URI = 'mongodb://localhost:27017/test_myapp'