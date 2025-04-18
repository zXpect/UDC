// Script para el panel de administración

document.addEventListener('DOMContentLoaded', function() {
    console.log('Panel de Administración - Cargado correctamente');
    
    // Confirmar eliminación de elementos
    document.querySelectorAll('.btn-danger').forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que deseas eliminar este elemento?')) {
                e.preventDefault();
            }
        });
    });
});