function toggleCalendar() {
    const calendar = document.getElementById('event-calendar');
    calendar.style.display = calendar.style.display === 'none' ? 'block' : 'none';
}

function toggleUpload(sectionId) {
    const details = document.getElementById(sectionId);
    details.style.display = details.style.display === 'none' ? 'block' : 'none';
}

function showForumTopics() {
    const forumTopics = document.getElementById('forum-topics');
    forumTopics.style.display = forumTopics.style.display === 'none' ? 'block' : 'none';
}

function showMeetingsList() {
    const meetingsList = document.getElementById('meetings-list');
    meetingsList.style.display = meetingsList.style.display === 'none' ? 'block' : 'none';
}

function createEvent(event) {
    event.preventDefault(); // Previene el comportamiento por defecto del formulario

    const eventName = document.getElementById('event-name').value;
    const eventDate = document.getElementById('event-date').value;

    // Aquí podrías enviar los datos a tu servidor
    console.log(`Evento creado: ${eventName} en la fecha ${eventDate}`);

    // Resetea el formulario
    document.getElementById('event-form').reset();
    alert(`Evento "${eventName}" creado para el ${eventDate}`);
}

function createMeeting(event) {
    event.preventDefault(); // Previene el comportamiento por defecto del formulario

    const meetingTitle = document.getElementById('meeting-title').value;
    const meetingDate = document.getElementById('meeting-date').value;
    const meetingTime = document.getElementById('meeting-time').value;

    // Aquí podrías enviar los datos a tu servidor
    console.log(`Reunión creada: ${meetingTitle} en la fecha ${meetingDate} a las ${meetingTime}`);

    // Resetea el formulario
    document.getElementById('meeting-form').reset();
    alert(`Reunión "${meetingTitle}" creada para el ${meetingDate} a las ${meetingTime}`);
}
function toggleCalendar() {
    const calendar = document.getElementById('event-calendar');
    calendar.style.display = (calendar.style.display === 'none' || calendar.style.display === '') ? 'block' : 'none';
}

function toggleUpload(section) {
    const sectionDetails = document.getElementById(section);
    sectionDetails.style.display = (sectionDetails.style.display === 'none' || sectionDetails.style.display === '') ? 'block' : 'none';
}

function showForumTopics() {
    const forumTopics = document.getElementById('forum-topics');
    forumTopics.style.display = (forumTopics.style.display === 'none' || forumTopics.style.display === '') ? 'block' : 'none';
}

function showMeetingsList() {
    const meetingsList = document.getElementById('meetings-list');
    meetingsList.style.display = (meetingsList.style.display === 'none' || meetingsList.style.display === '') ? 'block' : 'none';
}
function createMeeting(event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma tradicional

    const title = document.getElementById('meeting-title').value;
    const date = document.getElementById('meeting-date').value;
    const time = document.getElementById('meeting-time').value;
    const link = document.getElementById('meeting-link').value;

    // Agregar la reunión a la lista
    const meetingList = document.getElementById('meeting-items');
    const listItem = document.createElement('li');
    listItem.innerHTML = `<strong>${title}</strong> - ${date} a las ${time} 
                          <a href="${link}" class="btn btn-link" target="_blank">Unirse a Video Llamada</a>`;
    meetingList.appendChild(listItem);

    // Limpiar el formulario
    document.getElementById('meeting-form').reset();
}

    function toggleMeetingsList() {
        const meetingsList = document.getElementById('meetings-list');
        meetingsList.style.display = meetingsList.style.display === 'none' ? 'block' : 'none';
    }

    