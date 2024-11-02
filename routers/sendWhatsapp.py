from fastapi import Depends, Request, APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from fastapi.templating import Jinja2Templates
import pywhatkit as pwk

router = APIRouter()

# Configuración de Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/templateNotificaciones", response_class=HTMLResponse)
async def template_Notificaciones(request: Request, db: Session = Depends(get_db)):
    telefonos = db.query(Usuario.nombre_usu, Usuario.telefono).all()

    return templates.TemplateResponse("notificaciones.html", {"request": request, "telefonos": telefonos})

@router.post("/sendWhatsappIncidence")
async def send_Whatsapp_Incidence(
    request: Request,
    telefono: str = Form(...),
    mensaje: str = Form(...),
    db: Session = Depends(get_db)
):

    usuario = db.query(Usuario).filter(Usuario.telefono == telefono).first()

    if usuario:
        try:
             # Enviar el mensaje de WhatsApp usando pywhatkit
            pwk.sendwhatmsg_instantly(
                telefono,
                f"¡Hola, *{usuario.nombre_usu}*! Queremos informarte de una incidencia que te concierne. "
                f"Detalles de la incidencia: *{mensaje}*. Por favor, no dudes en contactarnos si necesitas más información.",
                15,
                True
            )
            return RedirectResponse(url="/templateNotificaciones", status_code=303)
        
        except:
            return templates.TemplateResponse("notificaciones.html", {"request": request, "msgExcept": "No se pudo enviar el mensaje"})


@router.post("/sendWhatsappEvent")
async def send_whatsapp_event(
    categoriaEvento: str = Form(...),
    mensaje: str = Form(...),
    fecha: str = Form(...),
    db: Session = Depends(get_db)
    ):

    usuarios = db.query(Usuario.nombre_usu, Usuario.telefono).all()

    # Eventos sociales
    if categoriaEvento == "1":
        for usuario in usuarios:
            if usuario.telefono:  # Verificar que el teléfono no esté vacío
                pwk.sendwhatmsg_instantly(
                    usuario.telefono, 
                    f"¡Hola, *{usuario.nombre_usu}*! Nos complace invitarte a un evento social que se llevará a cabo en nuestro conjunto el día *{fecha}*. Detalles del evento: *{mensaje}*. ¡Esperamos contar con tu presencia!",
                    wait_time=15,
                    tab_close=True
                )

        # Redirigir después de enviar los mensajes
        return RedirectResponse(url="/templateNotificaciones", status_code=303)
    
    # Eventos administrativos
    if categoriaEvento == "2":
        for usuario in usuarios:
            if usuario.telefono:
                pwk.sendwhatmsg_instantly(
                    usuario.telefono, 
                    f"¡Hola, *{usuario.nombre_usu}*! Te recordamos que próximamente se realizará una reunión administrativa en el conjunto el día *{fecha}*. Detalles de la reunión: *{mensaje}*. Tu participación es importante.",
                    wait_time=15,
                    tab_close=True
                )

        return RedirectResponse(url="/templateNotificaciones", status_code=303)
    
    # Mantenimiento y servicios
    if categoriaEvento == "3":
        for usuario in usuarios:
            if usuario.telefono:
                pwk.sendwhatmsg_instantly(
                    usuario.telefono, 
                    f"¡Hola, *{usuario.nombre_usu}*! Te informamos que se realizará una actividad de mantenimiento en el conjunto el día *{fecha}*. Detalles de la actividad: *{mensaje}*. Agradecemos tu comprensión.",
                    wait_time=15,
                    tab_close=True
                )

        return RedirectResponse(url="/templateNotificaciones", status_code=303)
    
    # Eventos deportivos
    if categoriaEvento == "4":
        for usuario in usuarios:
            if usuario.telefono:
                pwk.sendwhatmsg_instantly(
                    usuario.telefono, 
                    f"¡Hola, *{usuario.nombre_usu}*! Queremos invitarte a un evento deportivo que organizaremos en el conjunto el día *{fecha}*. Detalles del evento: *{mensaje}*. ¡Anímate a participar y disfruta de la actividad!",
                    wait_time=15,
                    tab_close=True
                )

        return RedirectResponse(url="/templateNotificaciones", status_code=303)
    
    # Actividades culturales y educativas
    if categoriaEvento == "5":
        for usuario in usuarios:
            if usuario.telefono:
                pwk.sendwhatmsg_instantly(
                    usuario.telefono, 
                    f"¡Hola, *{usuario.nombre_usu}*! Te invitamos a participar en una actividad cultural y educativa en nuestro conjunto el día *{fecha}*. Detalles de la actividad: *{mensaje}*. ¡No te lo pierdas!",
                    wait_time=15,
                    tab_close=True
                )

        return RedirectResponse(url="/templateNotificaciones", status_code=303)
    
    # Avisos generales
    if categoriaEvento == "6":
        for usuario in usuarios:
            if usuario.telefono:
                pwk.sendwhatmsg_instantly(
                    usuario.telefono, 
                    f"¡Hola, *{usuario.nombre_usu}*! Te informamos sobre un aviso importante relacionado con el conjunto el día *{fecha}*. Detalles del aviso: *{mensaje}*. Si tienes preguntas, por favor contáctanos.",
                    wait_time=15,
                    tab_close=True
                )

        return RedirectResponse(url="/templateNotificaciones", status_code=303)