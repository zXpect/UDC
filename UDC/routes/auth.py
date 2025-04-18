from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__)

# Datos temporales de usuarios para simular autenticación
temp_users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'teacher': {'password': 'teacher123', 'role': 'teacher'},
    'student': {'password': 'student123', 'role': 'student'}
}

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in temp_users and temp_users[username]['password'] == password:
            # Simulación de inicio de sesión exitoso (sin manejo real de sesiones aún)
            role = temp_users[username]['role']
            if role == 'admin':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('public.index'))
        else:
            # Simulación de error
            return render_template('auth/login.html', error="Usuario o contraseña incorrectos")
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    # Simulación de cierre de sesión (sin manejo real de sesiones aún)
    return redirect(url_for('public.index'))