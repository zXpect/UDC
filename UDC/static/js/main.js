// Script principal para la aplicación con animaciones mejoradas

document.addEventListener('DOMContentLoaded', function() {
    console.log('NetSchool - Sistema de Gestión de Contenidos cargado correctamente');
    
    // Inicializar tooltips de Bootstrap si existen
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    // Animación para el navbar al hacer scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-lg');
                navbar.style.padding = '0.5rem 1rem';
            } else {
                navbar.classList.remove('shadow-lg');
                navbar.style.padding = '1rem';
            }
        });
    }

    // Animación para cards cuando están visibles
    const animateOnScroll = function() {
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;
            
            if (cardPosition < screenPosition) {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }
        });
    };

    // Inicialmente ocultar las cards para animarlas cuando sean visibles
    document.querySelectorAll('.card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.5s ease';
    });

    // Detectar cuando se hace scroll para animar elementos
    window.addEventListener('scroll', animateOnScroll);
    // Ejecutar una vez al cargar la página
    animateOnScroll();

    // Añadir efecto hover para los iconos en los servicios
    const serviceIcons = document.querySelectorAll('.card i.fas, .card i.far, .card i.fab');
    serviceIcons.forEach(icon => {
        icon.addEventListener('mouseover', function() {
            this.style.transform = 'scale(1.2) rotate(5deg)';
            this.style.color = '#00C853'; // Acento verde más brillante
        });
        
        icon.addEventListener('mouseout', function() {
            this.style.transform = 'scale(1) rotate(0)';
            this.style.color = '#007B3E'; // Verde principal
        });
    });

    // Animación para botones
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseover', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseout', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Efecto de enfoque para el formulario de contacto
    const formInputs = document.querySelectorAll('.form-control');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'translateX(5px)';
            this.style.borderLeftWidth = '3px';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'translateX(0)';
            this.style.borderLeftWidth = '1px';
        });
    });

    // Animación para el menú de navegación en móviles
    const navToggler = document.querySelector('.navbar-toggler');
    if (navToggler) {
        navToggler.addEventListener('click', function() {
            document.querySelector('.navbar-collapse').classList.toggle('animated-navbar');
        });
    }

    // Añadir efecto de pulso a elementos importantes
    document.querySelectorAll('.jumbotron .btn-primary').forEach(btn => {
        btn.classList.add('pulse');
    });
});