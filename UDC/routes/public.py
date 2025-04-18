from flask import Blueprint, render_template

public = Blueprint('public', __name__)

@public.route('/')
def index():
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
    return render_template('index.html', events=temp_events[:3])

@public.route('/about')
def about():
    return render_template('public/about.html')

@public.route('/events')
def events():
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
    return render_template('public/events.html', events=temp_events)

@public.route('/contact')
def contact():
    return render_template('public/contact.html')