from fastapi import Depends, Request, APIRouter, Form, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from fastapi.templating import Jinja2Templates
import pywhatkit as pwk
from tempfile import NamedTemporaryFile

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

router = APIRouter()

@router.post("/sendWhatsappIncidenceResi")
async def send_Whatsapp_Incidence(
    img: str = File(None),  # Parámetro img opcional para una imagen
    mensaje: str = Form(...),
    db: Session = Depends(get_db)
):
    # Obtener el primer administrador
    admin = db.query(Usuario.nombre_usu, Usuario.telefono).filter(Usuario.id_rol == 1).first()

    if admin and admin.telefono:  # Verificar que el admin tenga teléfono
        # Si no hay imagen, enviar solo el mensaje de texto
        if not img:
            pwk.sendwhatmsg_instantly(
                phone_no = admin.telefono,
                message = f"¡Hola, *{admin.nombre_usu}*! Te informamos que un residente ha reportado una nueva incidencia. \nDetalles de la incidencia: *{mensaje}*.",
                wait_time=15,
                tab_close=True
            )
        # Si hay imagen, enviar el mensaje y la imagen
        """else:
            pwk.sendwhats_image(
                receiver=admin.telefono,
                img_path= img,
                caption= f"¡Hola, *{admin.nombre_usu}*! Te informamos que un residente ha reportado una nueva incidencia. \nDetalles de la incidencia: *{mensaje}*.",
                wait_time= 10,
                tab_close= True
            )"""

    # Redirigir después de enviar el mensaje o la imagen
    return RedirectResponse(url="/templateNotificacionesResi", status_code=303)


