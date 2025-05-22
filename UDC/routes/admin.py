from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Event

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def dashboard():
    events = Event.find_all()
    return render_template('admin/dashboard.html', events=events)

@admin.route('/events')
def events():
    events = Event.find_all()
    return render_template('admin/events.html', events=events)

@admin.route('/events/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        try:
            Event.create(
                title=request.form.get('title'),
                date=request.form.get('date'),
                time=request.form.get('time'),
                location=request.form.get('location'),
                description=request.form.get('description')
            )
            flash('Evento creado exitosamente', 'success')
            return redirect(url_for('admin.events'))
        except Exception as e:
            flash('Error al crear el evento', 'error')
    
    return render_template('admin/event_form.html')

@admin.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.find_by_id(event_id)
    
    if not event:
        flash('Evento no encontrado', 'error')
        return redirect(url_for('admin.events'))
    
    if request.method == 'POST':
        try:
            Event.update(
                event_id,
                title=request.form.get('title'),
                date=request.form.get('date'),
                time=request.form.get('time'),
                location=request.form.get('location'),
                description=request.form.get('description')
            )
            flash('Evento actualizado exitosamente', 'success')
            return redirect(url_for('admin.events'))
        except Exception as e:
            flash('Error al actualizar el evento', 'error')
    
    return render_template('admin/event_form.html', event=event)

@admin.route('/events/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    try:
        Event.delete(event_id)
        flash('Evento eliminado exitosamente', 'success')
    except Exception as e:
        flash('Error al eliminar el evento', 'error')
    
    return redirect(url_for('admin.events'))