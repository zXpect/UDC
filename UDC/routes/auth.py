from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Por favor ingresa usuario y contraseña', 'error')
            return render_template('auth/login.html')
        
        try:
            user = User.find_by_username(username)
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
                # Configurar sesión
                session['user_id'] = str(user['_id'])
                session['username'] = user['username']
                session['role'] = user['role']
                
                flash(f'Bienvenido {username}', 'success')
                
                if user['role'] == 'admin':
                    return redirect(url_for('admin.dashboard'))
                else:
                    return redirect(url_for('public.index'))
            else:
                flash('Usuario o contraseña incorrectos', 'error')
                return render_template('auth/login.html')
        except Exception as e:
            flash('Error al procesar el inicio de sesión', 'error')
            return render_template('auth/login.html')
    
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validaciones básicas
        if not all([username, email, password, confirm_password]):
            flash('Todos los campos son obligatorios', 'error')
            return render_template('auth/register.html')
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return render_template('auth/register.html')
        
        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return render_template('auth/register.html')
        
        try:
            # Verificar si el usuario ya existe
            if User.find_by_username(username):
                flash('El nombre de usuario ya existe', 'error')
                return render_template('auth/register.html')
            
            if User.find_by_email(email):
                flash('El email ya está registrado', 'error')
                return render_template('auth/register.html')
            
            # Crear nuevo usuario
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            User.create(
                username=username,
                email=email,
                password=hashed_password,
                role='user'  # Por defecto los nuevos usuarios son 'user'
            )
            
            flash('Usuario registrado exitosamente. Ya puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
            
        except Exception as e:
            flash('Error al registrar el usuario', 'error')
            return render_template('auth/register.html')
    
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    # Limpiar la sesión
    username = session.get('username', 'Usuario')
    session.clear()
    flash(f'Hasta luego {username}', 'info')
    return redirect(url_for('public.index'))

# Función auxiliar para verificar si el usuario está logueado
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# Función auxiliar para verificar si el usuario es admin
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'error')
            return redirect(url_for('auth.login'))
        if session.get('role') != 'admin':
            flash('No tienes permisos para acceder a esta página', 'error')
            return redirect(url_for('public.index'))
        return f(*args, **kwargs)
    return decorated_function