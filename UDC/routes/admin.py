from flask import Blueprint, render_template, request, redirect, url_for

admin = Blueprint('admin', __name__, url_prefix='/admin')

# Datos temporales para simular eventos
temp_events = [
    {
        'id': 1,
        'title': 'Reunión de Padres',
        'date': '2025-05-15',
        'time': '18:00',
        'location': 'Auditorio Principal',
        'description': 'Reunión informativa para padres de familia.'
    },
    {
        'id': 2,
        'title': 'Día del Maestro',
        'date': '2025-05-20',
        'time': '10:00',
        'location': 'Patio Central',
        'description': 'Celebración por el día del maestro.'
    }
]

@admin.route('/')
def dashboard():
    return render_template('admin/dashboard.html', events=temp_events)

@admin.route('/events')
def events():
    return render_template('admin/events.html', events=temp_events)

@admin.route('/events/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        # Aquí se procesaría el formulario (simulado por ahora)
        return redirect(url_for('admin.events'))
    return render_template('admin/event_form.html')

@admin.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    # Simulación de obtención de evento por ID
    event = next((e for e in temp_events if e['id'] == event_id), None)
    
    if not event:
        return redirect(url_for('admin.events'))
    
    if request.method == 'POST':
        # Aquí se procesaría el formulario (simulado por ahora)
        return redirect(url_for('admin.events'))
    
    return render_template('admin/event_form.html', event=event)