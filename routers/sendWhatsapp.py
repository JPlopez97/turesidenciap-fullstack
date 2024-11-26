from fastapi import Depends, Request, APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from fastapi.templating import Jinja2Templates
import pywhatkit as pwk

sendWhatsappRouter = APIRouter()

# Configuración de Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@sendWhatsappRouter.get("/templateNotificaciones", response_class=HTMLResponse)
async def template_Notificaciones(request: Request, db: Session = Depends(get_db)):
    telefonos = db.query(Usuario.nombre_usu, Usuario.telefono).all()

    return templates.TemplateResponse("notificaciones.html", {"request": request, "telefonos": telefonos, "active_page": request.url.path})

@sendWhatsappRouter.post("/sendWhatsappIncidence")
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
                15
            )
            return RedirectResponse(url="/templateNotificaciones", status_code=303)
        
        except:
            return templates.TemplateResponse("notificaciones.html", {"request": request, "msgExcept": "No se pudo enviar el mensaje"})


@sendWhatsappRouter.post("/sendWhatsappEvent")
async def send_whatsapp_event(
    categoriaEvento: str = Form(...),
    mensaje: str = Form(...),
    fecha: str = Form(...),
    db: Session = Depends(get_db)
):
    usuarios = db.query(Usuario.nombre_usu, Usuario.telefono).all()

    # Diccionario para asociar categorías con mensajes
    mensajes_por_categoria = {
        "1": f"¡Hola, *{{nombre}}*! Nos complace invitarte a un evento social que se llevará a cabo en nuestro conjunto el día *{fecha}*. Detalles del evento: *{mensaje}*. ¡Esperamos contar con tu presencia!",
        "2": f"¡Hola, *{{nombre}}*! Te recordamos que próximamente se realizará una reunión administrativa en el conjunto el día *{fecha}*. Detalles de la reunión: *{mensaje}*. Tu participación es importante.",
        "3": f"¡Hola, *{{nombre}}*! Te informamos que se realizará una actividad de mantenimiento en el conjunto el día *{fecha}*. Detalles de la actividad: *{mensaje}*. Agradecemos tu comprensión.",
        "4": f"¡Hola, *{{nombre}}*! Queremos invitarte a un evento deportivo que organizaremos en el conjunto el día *{fecha}*. Detalles del evento: *{mensaje}*. ¡Anímate a participar y disfruta de la actividad!",
        "5": f"¡Hola, *{{nombre}}*! Te invitamos a participar en una actividad cultural y educativa en nuestro conjunto el día *{fecha}*. Detalles de la actividad: *{mensaje}*. ¡No te lo pierdas!",
        "6": f"¡Hola, *{{nombre}}*! Te informamos sobre un aviso importante relacionado con el conjunto el día *{fecha}*. Detalles del aviso: *{mensaje}*. Si tienes preguntas, por favor contáctanos."
    }

    # Obtener el mensaje correspondiente a la categoría
    mensaje_personalizado = mensajes_por_categoria.get(categoriaEvento)

    if not mensaje_personalizado:
        return {"error": "Categoría de evento no válida"}

    # Enviar mensajes a los usuarios
    for usuario in usuarios:
        if usuario.telefono:  # Verificar que el teléfono no esté vacío
            mensaje_final = mensaje_personalizado.format(nombre=usuario.nombre_usu)
            pwk.sendwhatmsg_instantly(
                usuario.telefono, 
                mensaje_final,
                wait_time=15
            )

    # Redirigir después de enviar los mensajes
    return RedirectResponse(url="/templateNotificaciones", status_code=303)