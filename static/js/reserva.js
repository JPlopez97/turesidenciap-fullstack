document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.querySelector("#formularioReserva form");

    formulario.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita que el formulario se envíe de inmediato

        // Validar campos
        const categoria = document.getElementById("categoria").value;
        const nombre = document.getElementById("nombre").value;
        const cedula = document.getElementById("cedula").value;
        const telefono = document.getElementById("telefono").value;
        const torre = document.getElementById("torre").value;
        const apartamento = document.getElementById("apartamento").value;
        const fecha = document.getElementById("fecha").value;
        const hora = document.getElementById("hora").value;

        if (categoria && nombre && cedula && telefono && torre && apartamento && fecha && hora) {
            // Si todos los campos son válidos, muestra un mensaje de confirmación
            alert(`Reserva realizada con éxito!\n\nDetalles:\nCategoría: ${categoria}\nNombre: ${nombre}\nCédula: ${cedula}\nTeléfono: ${telefono}\nTorre: ${torre}\nApartamento: ${apartamento}\nFecha: ${fecha}\nHora: ${hora}`);
            // Aquí puedes agregar la lógica para enviar los datos al servidor, si es necesario.
            formulario.reset(); // Reinicia el formulario
        } else {
            alert("Por favor, completa todos los campos requeridos.");
        }
    });
});
