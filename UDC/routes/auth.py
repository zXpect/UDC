from flask import Blueprint, render_template, request, redirect, url_for, flash, session  
from models import User  
  
auth = Blueprint('auth', __name__)  
  
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
  
@auth.route('/logout')  
def logout():  
    session.clear()  
    flash('Has cerrado sesión exitosamente', 'success')  
    return redirect(url_for('public.index'))  
  
def login_required(f):  
    from functools import wraps  
    @wraps(f)  
    def decorated_function(*args, **kwargs):  
        if not session.get('logged_in'):  
            return redirect(url_for('auth.login'))  
        return f(*args, **kwargs)  
    return decorated_function  
  
def admin_required(f):  
    from functools import wraps  
    @wraps(f)  
    def decorated_function(*args, **kwargs):  
        if not session.get('logged_in') or session.get('role') != 'admin':  
            flash('Acceso denegado. Se requieren permisos de administrador.', 'error')  
            return redirect(url_for('auth.login'))  
        return f(*args, **kwargs)  
    return decorated_function