from fastapi import FastAPI, Depends, Request, APIRouter, Form
from fastapi.responses import HTMLResponse  # Para devolver respuestas HTML
from sqlalchemy.orm import Session  # Manejo de sesiones con SQLAlchemy
from database import SessionLocal  # Sesión de DB configurada
from models import Usuario, Residente  # Modelos de la base de datos
from passlib.context import CryptContext  # Para manejar el cifrado de contraseñas
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML mediante Jinja2
from fastapi.staticfiles import StaticFiles # Para trabajar con los css, js, img, etc.


register_user_router = APIRouter(tags=["registerUser"], 
                   responses={404: {"message": "No encontrado"}})

# Contexto de cifrado de contraseñas. Se usa el esquema 'bcrypt' para cifrar y verificar contraseñas.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

# Dependencia para obtener la sesión de base de datos
def get_db():
    # Crear nueva sesión de base de datos
    db = SessionLocal()
    try:
        # 'yield' devuelve la sesión para que se use en el request actual
        yield db
    finally:
        # Cerrar la sesión de base de datos al terminar el request
        db.close()

# Hash de contraseña
def hash_password(password: str):
    return pwd_context.hash(password)

# Ruta para mostrar el formulario de registro de usuarios
@register_user_router.get("/templateRegister", response_class=HTMLResponse)
async def templateRegister(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@register_user_router.post("/register_user")
async def register_user(
    request: Request,
    cc_usuario: int = Form(...),
    nombre_usu: str = Form(...),
    correo_electronico: str = Form(...),
    telefono: str = Form(...),
    contrasena: str = Form(...),
    id_rol: int = Form(...),
    db: Session = Depends(get_db)
):
    
     # Agregar el prefijo +57 al número si no está presente
    if not telefono.startswith("+57"):
        telefono = f"+57{telefono}"
    
    user = db.query(Usuario).filter(Usuario.cc_usuario == cc_usuario).first()
    correo = db.query(Usuario).filter(Usuario.correo_electronico == correo_electronico).first()
    tel = db.query(Usuario).filter(Usuario.telefono == telefono).first()

    if user or correo or tel:
        return templates.TemplateResponse("register.html", {"request": request, "error": "El usuario ya existe"})

        
    nuevo_usuario = Usuario(
        cc_usuario = cc_usuario,
        nombre_usu=nombre_usu,
        correo_electronico=correo_electronico,
        telefono = telefono,
        contrasena= hash_password(contrasena),
        id_rol=id_rol
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    if id_rol == 2:

        # Registrar al usuario en la tabla de residentes
        nuevo_residente = Residente(
        cc_usuario=nuevo_usuario.cc_usuario
        )

        # Guardar los cambios en la base de datos
        db.add(nuevo_residente)
        db.commit()

    return templates.TemplateResponse("register.html", {"request": request, "success": "Usuario registrado exitosamente"})