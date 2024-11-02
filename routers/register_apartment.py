from fastapi import Depends, Request, APIRouter, Form
from fastapi.responses import HTMLResponse  # Para devolver respuestas HTML
from sqlalchemy.orm import Session  # Manejo de sesiones con SQLAlchemy
from database import SessionLocal  # Sesión de DB configurada
from models import Apartamento  # Modelos de la base de datos
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML mediante Jinja2


router = APIRouter(tags=["registerApartment"], 
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

# Ruta para mostrar el formulario de registro de usuarios
@router.get("/templateRegisterApartment", response_class=HTMLResponse)
async def templateRegister(request: Request):
    return templates.TemplateResponse("registerApartment.html", {"request": request})

@router.post("/register_apartment")
async def register_apartment(
    request: Request,
    num_apto: int = Form(...),
    piso_apto: int = Form(...),
    torre_apto: int = Form(...),
    db: Session = Depends(get_db)
):
    
    apartamentoExistente = db.query(Apartamento).filter(Apartamento.num_apto == num_apto, Apartamento.piso_apto == piso_apto, Apartamento.torre_apto == torre_apto).first()

    if apartamentoExistente:
        return templates.TemplateResponse("registerApartment.html", {"request": request, "error": "El apartamento ya existe"})

        
    nuevo_apartamento = Apartamento(
        num_apto = num_apto,
        piso_apto = piso_apto,
        torre_apto = torre_apto,
        estado_apto = 'disponible'
    )
    
    db.add(nuevo_apartamento)
    db.commit()
    db.refresh(nuevo_apartamento)

    return templates.TemplateResponse("registerApartment.html", {"request": request, "success": "Apartamento registrado exitosamente"})