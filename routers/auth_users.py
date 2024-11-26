from fastapi import FastAPI, Depends, Request, APIRouter, HTTPException, Header
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario, Residente, Apartamento
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from functions_jwt import write_token, validate_token
from fastapi.security import HTTPBearer
from fastapi.staticfiles import StaticFiles


pwd_context = CryptContext(schemes=["bcrypt"])
auth_router = APIRouter(tags=["auth"])
templates = Jinja2Templates(directory="templates")
security = HTTPBearer()

auth_router.mount("/static", StaticFiles(directory="static"), name="static")

# Dependencia para obtener sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Verificar contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Autenticar usuario
def authenticate(username: str, password: str, db: Session):
    user = db.query(Usuario).filter(Usuario.nombre_usu == username).first()
    if user is None or not verify_password(password, user.contrasena):
        return None
    return user

# Ruta para mostrar el formulario de login
@auth_router.get("/templateLogin", response_class=HTMLResponse)
async def templateLogin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Ruta para procesar el login
@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate(form_data.username, form_data.password, db)

    if not user:
        # Mostrar error si las credenciales son incorrectas
        return templates.TemplateResponse("login.html", {
            "request": {},
            "error": "Usuario o contraseña incorrectos"
        })
    
    # Crear token JWT
    token = write_token({"cc_usuario": user.cc_usuario, "id_rol": user.id_rol})
    residente = db.query(Residente, Apartamento).join(Apartamento).filter(Residente.id_apto == Apartamento.id_apto).first()

    # Redirigir según el rol del usuario
    if user.id_rol == 1:  # Administrador
        response = templates.TemplateResponse("indexAdmin.html", {"request": {},
        "user_name": user.nombre_usu,
        "user_email": user.correo_electronico,
        "user_phone": user.telefono,
        "user_role": "Administrador",
        "active_page": "/templateIndexAdmin"
    })
    if user.id_rol == 3: #Propietario
        response = templates.TemplateResponse("indexAdminpro.html", {"request": {},
        "user_name": user.nombre_usu,
        "user_email": user.correo_electronico,
        "user_phone": user.telefono,
        "user_role": "Propietario",
        "active_page": "/templateIndexAdminpro"
        })
    if user.id_rol == 2:  # Residente
        apartamento = residente.Apartamento
        response = templates.TemplateResponse("indexResidente.html", {"request": {},
        "user_name": user.nombre_usu,
        "user_email": user.correo_electronico,
        "user_phone": user.telefono,
        "user_apartment": apartamento.num_apto,
        "user_tower": apartamento.torre_apto,
        "user_role": "Residente",
        "active_page": "/templateIndexResidente"
    })

    response.set_cookie(key="access_token", value=token, httponly=True, secure=True)
    return response  