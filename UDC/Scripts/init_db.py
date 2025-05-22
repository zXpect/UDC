from models import User, Event  
import bcrypt  
  
# Crear usuarios iniciales  
users = [  
    {'username': 'admin', 'password': bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()), 'role': 'admin'},  
    {'username': 'teacher', 'password': bcrypt.hashpw('teacher123'.encode('utf-8'), bcrypt.gensalt()), 'role': 'teacher'},  
    {'username': 'student', 'password': bcrypt.hashpw('student123'.encode('utf-8'), bcrypt.gensalt()), 'role': 'student'}  
]  
  
for user in users:  
    User.collection.insert_one(user)