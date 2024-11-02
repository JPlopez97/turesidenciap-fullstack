from fastapi import Depends, Request, APIRouter, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from fastapi.templating import Jinja2Templates
import smtplib

router = APIRouter()

# Configuración de Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('fe.lopez10@ciaf.edu.co', '1004700843')

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/getEmails", response_class=HTMLResponse)
async def get_Email(request: Request, db: Session = Depends(get_db)):
    correos = db.query(Usuario.nombre_usu, Usuario.correo_electronico).all()

    return templates.TemplateResponse("notificaciones.html", {"request": request, "correos": correos})

@router.post("/sendEmail")
async def send_Email(
    correo: str = Form(...),
    mensaje: str = Form(...)
    ):
    server.sendmail('fe.lopez10@ciaf.edu.co', correo, mensaje)