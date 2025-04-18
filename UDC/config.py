import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    # Aquí agregaremos configuraciones de base de datos más adelante