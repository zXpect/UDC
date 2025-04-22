// Script para el panel de administración con animaciones mejoradas

document.addEventListener('DOMContentLoaded', function() {
    console.log('Panel de Administración - Cargado correctamente');
    
    // Añadir clase para animación de entrada
    document.querySelectorAll('.card, .table').forEach(function(element, index) {
        setTimeout(function() {
            element.classList.add('admin-animate-in');
        }, index * 100);
    });
    
    // Confirmar eliminación de elementos
    document.querySelectorAll('.btn-danger').forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que deseas eliminar este elemento?')) {
                e.preventDefault();
            }
        });
    });

    // Animación para íconos en sidebar
    document.querySelectorAll('.list-group-item i').forEach(function(icon) {
        icon.originalColor = getComputedStyle(icon).color;
        
        icon.addEventListener('mouseover', function() {
            this.style.transform = 'scale(1.3) rotate(10deg)';
            this.style.color = '#00C853';
        });
        
        icon.addEventListener('mouseout', function() {
            this.style.transform = 'scale(1) rotate(0)';
            this.style.color = this.originalColor;
        });
    });

    // Efecto de hover para filas de tablas
    document.querySelectorAll('tbody tr').forEach(function(row) {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = 'rgba(0, 123, 62, 0.05)';
            this.style.transform = 'translateX(5px)';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
            this.style.transform = 'translateX(0)';
        });
    });

    // Efecto para tarjetas de estadísticas
    document.querySelectorAll('.card-body .fa-3x').forEach(function(icon) {
        icon.style.transition = 'all 0.5s ease';
        
        icon.parentElement.parentElement.addEventListener('mouseenter', function() {
            icon.style.transform = 'rotate(15deg) scale(1.2)';
        });
        
        icon.parentElement.parentElement.addEventListener('mouseleave', function() {
            icon.style.transform = 'rotate(0) scale(1)';
        });
    });

    // Efecto para botones
    document.querySelectorAll('.btn').forEach(function(button) {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
            this.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });

    // Contador animado para estadísticas
    function animateCounter(element, targetValue) {
        let currentValue = 0;
        const duration = 1500;
        const frameRate = 60;
        const totalFrames = Math.round(duration / (1000 / frameRate));
        const increment = targetValue / totalFrames;

        const counter = setInterval(() => {
            currentValue += increment;
            if (currentValue >= targetValue) {
                currentValue = targetValue;
                clearInterval(counter);
            }
            element.textContent = Math.floor(currentValue);
        }, 1000 / frameRate);
    }

    // Animar contadores cuando son visibles
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = entry.target.querySelectorAll('h2.mb-0');
                counters.forEach(counter => {
                    const targetValue = parseInt(counter.textContent, 10);
                    counter.textContent = '0';
                    animateCounter(counter, targetValue);
                });
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    // Observar elementos con estadísticas
    document.querySelectorAll('.card.bg-primary, .card.bg-success, .card.bg-info').forEach(card => {
        observer.observe(card);
    });
});