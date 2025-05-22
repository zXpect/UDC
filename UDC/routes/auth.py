from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps
from models import User

auth = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in') or session.get('role') != 'admin':
            flash('Acceso denegado. Se requieren permisos de administrador.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.verify_password(username, password)
        if user:
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['role'] = user['role']
            session['logged_in'] = True
            
            if user['role'] == 'admin':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('public.index'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return render_template('auth/login.html', error="Usuario o contraseña incorrectos")
    
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role', 'student')  # Por defecto estudiante
        
        # Validaciones
        if not username or not password or not confirm_password:
            flash('Todos los campos son obligatorios', 'error')
            return render_template('auth/register.html')
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return render_template('auth/register.html')
        
        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return render_template('auth/register.html')
        
        # Verificar si el usuario ya existe
        existing_user = User.find_by_username(username)
        if existing_user:
            flash('El nombre de usuario ya existe', 'error')
            return render_template('auth/register.html')
        
        # Crear nuevo usuario
        try:
            User.create_user(username, password, role)
            flash('Usuario registrado exitosamente. Puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('Error al registrar usuario', 'error')
            return render_template('auth/register.html')
    
    return render_template('auth/register.html')

@auth.route('/profile')
@login_required
def profile():
    user_info = {
        'username': session.get('username'),
        'role': session.get('role'),
        'user_id': session.get('user_id')
    }
    return render_template('auth/profile.html', user=user_info)

@auth.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión exitosamente', 'success')
    return redirect(url_for('public.index'))