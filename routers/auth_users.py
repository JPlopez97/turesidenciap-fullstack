from fastapi import FastAPI, Depends, Request, APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse  # Para devolver respuestas HTML
from sqlalchemy.orm import Session  # Manejo de sesiones con SQLAlchemy
from database import SessionLocal  # Sesión de base de datos configurada
from models import Usuario  # Modelos de la base de datos
from passlib.context import CryptContext  # Para manejar el cifrado de contraseñas
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm  # Para manejar OAuth2 y formularios
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML
from datetime import datetime, timedelta, timezone  # Manejo de tiempo y expiración de tokens
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from pydantic import BaseModel

SECRET_KEY = "8da4f260c44aac7aab262d1730e23556f38065782bff6ebbfd07b7bb967a1c46"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Contexto de cifrado de contraseñas. Se usa el esquema 'bcrypt' para cifrar y verificar contraseñas.
pwd_context = CryptContext(schemes=["bcrypt"])

router = APIRouter(tags=["login"],
                   responses={404: {"message": "No encontrado"}})

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

# Función para verificar la contraseña. Comparanmdo la contraseña en texto plano con su versión cifrada.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Se usa pwd_context para verificar que la contraseña en texto plano coincida con la cifrada
    return pwd_context.verify(plain_password, hashed_password)

# Función de autenticación. Busca al usuario en la base de datos y verifica su contraseña.
def authenticate(username: str, password: str, db: Session):
    # Consulta en la base de datos para buscar al usuario por su nombre de usuario
    user = db.query(Usuario).filter(Usuario.nombre_usu == username).first()
    
    # Si el usuario no existe o la contraseña no es correcta, devolvemos None
    if user is None or not verify_password(password, user.contrasena):
        return None
    
    # Si la autenticación es exitosa, devolvemos al usuario
    return user

# Ruta para mostrar el formulario de login
@router.get("/templateLogin", response_class=HTMLResponse)
async def templateLogin(request: Request, token: str = Depends(oauth2_scheme)):
    print(token)
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Llamamos a la función 'authenticate' para verificar si el usuario existe y la contraseña es correcta
    user = authenticate(form_data.username, form_data.password, db)
    
    # Si la autenticación falla, devuelve un template con un mensaje de error
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Usuario o contraseña incorrectos"})
    
    # Redirigir según el rol del usuario
    if user.id_rol == 1:
        return templates.TemplateResponse("indexAdmin.html", {"request": request})
    
    return templates.TemplateResponse("indexResidente.html", {"request": request})