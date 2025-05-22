from models import User, Event  
import bcrypt  
  
def init_database():  
    # Crear usuarios iniciales  
    users = [  
        {'username': 'admin', 'password': 'admin123', 'role': 'admin'},  
        {'username': 'teacher', 'password': 'teacher123', 'role': 'teacher'},  
        {'username': 'student', 'password': 'student123', 'role': 'student'}  
    ]  
      
    for user_data in users:  
        existing_user = User.find_by_username(user_data['username'])  
        if not existing_user:  
            User.create_user(user_data['username'], user_data['password'], user_data['role'])  
            print(f"Usuario {user_data['username']} creado")  
        else:  
            print(f"Usuario {user_data['username']} ya existe")  
      
    # Crear eventos iniciales  
    events = [  
        {  
            'title': 'Reunión de Padres',  
            'date': '2025-05-15',  
            'time': '18:00',  
            'location': 'Auditorio Principal',  
            'description': 'Reunión informativa para padres de familia.'  
        },  
        {  
            'title': 'Día del Maestro',  
            'date': '2025-05-20',  
            'time': '10:00',  
            'location': 'Patio Central',  
            'description': 'Celebración por el día del maestro.'  
        }  
    ]  
      
    for event_data in events:  
        Event.create(**event_data)  
        print(f"Evento '{event_data['title']}' creado")  
  
if __name__ == '__main__':  
    init_database()  
    print("Base de datos inicializada correctamente")