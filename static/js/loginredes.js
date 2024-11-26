const openModalBtn = document.getElementById('openModalBtn');
const modalElement = new bootstrap.Modal(document.getElementById('aboutUsModal'));

// Abrir el modal al hacer clic en el botón
openModalBtn.addEventListener('click', function(event) {
    event.preventDefault(); // Prevenir la acción por defecto (no recargar la página)
    modalElement.show(); // Abrir el modal
});