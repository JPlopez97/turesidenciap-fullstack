document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Obtener los valores del formulario
    const nombre = document.getElementById('nombre').value;
    const cedula = document.getElementById('cedula').value;
    const torre = document.getElementById('torre').value;
    const apartamento = document.getElementById('apartamento').value;
    const fecha = document.getElementById('fecha').value;
    const mes = document.getElementById('mes').value;

    // Crear el PDF usando jsPDF
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Agregar contenido al PDF
    doc.text('Informe de Reserva', 10, 10);
    doc.text(`Nombre: ${nombre}`, 10, 20);
    doc.text(`Cédula: ${cedula}`, 10, 30);
    doc.text(`Torre: ${torre}`, 10, 40);
    doc.text(`Apartamento: ${apartamento}`, 10, 50);
    doc.text(`Fecha: ${fecha}`, 10, 60);
    doc.text(`Mes: ${mes}`, 10, 70);
    
    // Descargar el PDF
    doc.save(`Informe_${nombre}.pdf`);

    // Resetear el formulario
    this.reset();
});
// Simulación de una base de datos de residentes
const residentes = {
    'Juan Pérez': { cedula: '123456789', apartamento: '101' },
    'María López': { cedula: '987654321', apartamento: '202' },
    'Carlos Gómez': { cedula: '456789123', apartamento: '303' },
};

function fillResidentDetails() {
    const nombre = document.getElementById('nombreResidente').value;
    const residente = residentes[nombre];

    if (residente) {
        document.getElementById('cedulaPayment').value = residente.cedula;
        document.getElementById('apartamentoPayment').value = residente.apartamento;
    } else {
        document.getElementById('cedulaPayment').value = '';
        document.getElementById('apartamentoPayment').value = '';
    }
}

function generatePaymentPDF(event) {
    event.preventDefault(); // Evita el envío del formulario
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const nombre = document.getElementById('nombreResidente').value;
    const cedula = document.getElementById('cedulaPayment').value;
    const apartamento = document.getElementById('apartamentoPayment').value;
    const reservaType = document.getElementById('reservasType').value;
    const monto = document.getElementById('paymentAmount').value;
    const mes = document.getElementById('monthPayment').value;
    const fechaPago = document.getElementById('paymentDate').value;

    doc.text('Registro de Pago de Reserva', 10, 10);
    doc.text(`Nombre del Residente: ${nombre}`, 10, 20);
    doc.text(`Cédula: ${cedula}`, 10, 30);
    doc.text(`Apartamento: ${apartamento}`, 10, 40);
    doc.text(`Tipo de Reserva: ${reservaType}`, 10, 50);
    doc.text(`Monto: ${monto}`, 10, 60);
    doc.text(`Mes: ${mes}`, 10, 70);
    doc.text(`Fecha de Pago: ${fechaPago}`, 10, 80);

    doc.save('pago_reserva.pdf'); // Guarda el PDF
}
const uploadedFiles = []; // Array para almacenar los archivos subidos

function uploadFile(event) {
    event.preventDefault(); // Evita el envío del formulario

    const fileInput = document.getElementById('fileInput');
    const fileDescription = document.getElementById('fileDescription');
    const file = fileInput.files[0];

    // Validar que haya un archivo
    if (file) {
        const fileData = {
            name: file.name,
            description: fileDescription.value,
            url: URL.createObjectURL(file), // Crear URL para acceder al archivo
        };

        uploadedFiles.push(fileData); // Agregar el archivo a la lista

        // Limpiar los campos del formulario
        fileInput.value = '';
        fileDescription.value = '';

        // Mostrar el archivo en la lista
        displayFiles();
    }
}

function displayFiles() {
    const fileList = document.getElementById('fileList');
    fileList.innerHTML = ''; // Limpiar la lista antes de mostrar

    uploadedFiles.forEach(file => {
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item';
        listItem.innerHTML = `
            <a href="${file.url}" download="${file.name}">${file.name}</a> - ${file.description}
        `;
        fileList.appendChild(listItem);
    });
}