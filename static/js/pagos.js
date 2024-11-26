// Datos simulados de pagos con más apartamentos
let payments = [
    { id: 1, cedula: '1234567890', name: 'Juan Pérez', tower: 'A', apartment: '101', date: '2024-11-10', status: 'pendiente' },
    { id: 2, cedula: '9876543210', name: 'Ana Gómez', tower: 'B', apartment: '202', date: '2024-11-11', status: 'realizado' },
    { id: 3, cedula: '1230984567', name: 'Carlos Rodríguez', tower: 'C', apartment: '303', date: '2024-11-09', status: 'Fallido' },
    { id: 4, cedula: '4567890123', name: 'Maria López', tower: 'A', apartment: '404', date: '2024-11-08', status: 'pendiente' },
    { id: 5, cedula: '6543210987', name: 'Luis Fernández', tower: 'B', apartment: '505', date: '2024-11-07', status: 'realizado' },
    { id: 6, cedula: '7891234560', name: 'Sofía Martínez', tower: 'C', apartment: '606', date: '2024-11-06', status: 'Fallido' },
    { id: 7, cedula: '8901234567', name: 'Andrés Gómez', tower: 'D', apartment: '707', date: '2024-11-05', status: 'pendiente' },
    { id: 8, cedula: '5678901234', name: 'Elena Sánchez', tower: 'A', apartment: '808', date: '2024-11-04', status: 'realizado' },
    { id: 9, cedula: '4321098765', name: 'Raúl Martínez', tower: 'B', apartment: '909', date: '2024-11-03', status: 'Fallido' },
    { id: 10, cedula: '4567890123', name: 'Sofia Martínez', tower: 'D', apartment: '1010', date: '2024-11-02', status: 'pendiente' }
];

// Función para renderizar los pagos en la tabla
function renderPayments(filteredPayments = payments) {
    const paymentList = document.getElementById('payment-list');
    paymentList.innerHTML = ''; // Limpiar la tabla antes de llenarla con datos

    filteredPayments.forEach(payment => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${payment.id}</td>
            <td>${payment.cedula}</td>
            <td>${payment.name}</td>
            <td>${payment.tower}</td>
            <td>${payment.apartment}</td>
            <td>${payment.date}</td>
            <td class="status-${payment.status}">${capitalizeFirstLetter(payment.status)}</td>
        `;
        paymentList.appendChild(row);
    });
}

// Función para capitalizar la primera letra de la palabra
function capitalizeFirstLetter(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

// Función para filtrar los pagos en base a la búsqueda
function searchPayments() {
    const searchCedula = document.getElementById('searchCedula').value.toLowerCase();
    const searchNombre = document.getElementById('searchNombre').value.toLowerCase();
    const searchApartamento = document.getElementById('searchApartamento').value.toLowerCase();
    const filterStatus = document.getElementById('filterStatus').value;

    const filteredPayments = payments.filter(payment => {
        const matchesCedula = payment.cedula.toLowerCase().includes(searchCedula);
        const matchesNombre = payment.name.toLowerCase().includes(searchNombre);
        const matchesApartamento = payment.apartment.toLowerCase().includes(searchApartamento);
        const matchesStatus = filterStatus ? payment.status === filterStatus : true;
        return matchesCedula && matchesNombre && matchesApartamento && matchesStatus;
    });

    renderPayments(filteredPayments); // Mostrar los pagos filtrados
}

// Función para actualizar el estado de todos los pagos
function updateAllPayments() {
    payments = payments.map(payment => {
        if (payment.status === 'pendiente') {
            payment.status = 'realizado';
        } else if (payment.status === 'realizado') {
            payment.status = 'Fallido';
        } else {
            payment.status = 'pendiente';
        }
        return payment;
    });
    renderPayments(); // Volver a renderizar los pagos con los nuevos estados
}

// Inicializar la tabla al cargar la página
renderPayments();