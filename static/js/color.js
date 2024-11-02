function getUserInfo() {
    const user = {
        name: "Juan Pérez",
        email: "juan.perez@example.com",
        phone: "555-1234",
        apartment: "101A",
        tower: "Torre 1",
        type: "Administrador",
    };

    document.getElementById("userName").innerText = user.name;
    document.getElementById("userEmail").innerText = user.email;
    document.getElementById("userPhone").innerText = user.phone;
    document.getElementById("userApartment").innerText = user.apartment;
    document.getElementById("userTower").innerText = user.tower;
    document.getElementById("userType").innerText = user.type;


// Funciones para los botones
document.getElementById("modifyProfile").addEventListener("click", function() {
    alert("Modificar Perfil");
});

document.getElementById("logout").addEventListener("click", function() {
    alert("Cerrar Sesión");
});

// Actualizamos la sección de información del usuario al cargar la página
document.addEventListener("DOMContentLoaded", getUserInfo);
}
