from flask import Blueprint, render_template, request, redirect, url_for, flash  
from models import Event  
from routes.auth import admin_required  
  
admin = Blueprint('admin', __name__)  
  
@admin.route('/')  
@admin_required  
def dashboard():  
    events = Event.find_all()  
    return render_template('admin/dashboard.html', events=events)  
  
@admin.route('/events')  
@admin_required  
def events():  
    events = Event.find_all()  
    return render_template('admin/events.html', events=events)  
  
@admin.route('/events/add', methods=['GET', 'POST'])  
@admin_required  
def add_event():  
    if request.method == 'POST':  
        title = request.form.get('title')  
        date = request.form.get('date')  
        time = request.form.get('time')  
        location = request.form.get('location')  
        description = request.form.get('description')  
          
        if title and date and time and location and description:  
            event_id = Event.create(title, date, time, location, description)  
            if event_id:  
                flash('Evento creado exitosamente', 'success')  
                return redirect(url_for('admin.events'))  
            else:  
                flash('Error al crear el evento', 'error')  
        else:  
            flash('Todos los campos son obligatorios', 'error')  
      
    return render_template('admin/event_form.html')  
  
@admin.route('/events/edit/<event_id>', methods=['GET', 'POST'])  
@admin_required  
def edit_event(event_id):  
    event = Event.find_by_id(event_id)  
      
    if not event:  
        flash('Evento no encontrado', 'error')  
        return redirect(url_for('admin.events'))  
      
    if request.method == 'POST':  
        title = request.form.get('title')  
        date = request.form.get('date')  
        time = request.form.get('time')  
        location = request.form.get('location')  
        description = request.form.get('description')  
          
        if title and date and time and location and description:  
            if Event.update(event_id, title, date, time, location, description):  
                flash('Evento actualizado exitosamente', 'success')  
                return redirect(url_for('admin.events'))  
            else:  
                flash('Error al actualizar el evento', 'error')  
        else:  
            flash('Todos los campos son obligatorios', 'error')  
      
    return render_template('admin/event_form.html', event=event)  
  
@admin.route('/events/delete/<event_id>')  
@admin_required  
def delete_event(event_id):  
    if Event.delete(event_id):  
        flash('Evento eliminado exitosamente', 'success')  
    else:  
        flash('Error al eliminar el evento', 'error')  
      
    return redirect(url_for('admin.events'))