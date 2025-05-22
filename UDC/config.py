import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb+srv://ballesterosmaik:R1RlAchx6A7RzhaW@cluster0.ocdhahx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'  
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY') or 'AIzaSyA6j7YaKesOKWEgaGTsNruStFRKH0pxeQY'
    SESSION_TYPE = 'filesystem'  
    SESSION_PERMANENT = False