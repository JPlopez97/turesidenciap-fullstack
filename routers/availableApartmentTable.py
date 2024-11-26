from fastapi import FastAPI, Depends, Request, APIRouter
from fastapi.responses import HTMLResponse  # Para devolver respuestas HTML
from sqlalchemy.orm import Session  # Manejo de sesiones con SQLAlchemy
from database import SessionLocal  # Sesión de base de datos configurada
from models import Usuario, Apartamento, Residente  # Modelos de la base de datos
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML mediante Jinja2
from fastapi.staticfiles import StaticFiles # Para trabajar con los css, js, img, etc.


availableApartmentTableRouter = APIRouter(tags=["getAvailableDepartments"], 
                   responses={404: {"message": "No encontrado"}})

# Configuración Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

availableApartmentTableRouter.mount("/static", StaticFiles(directory="static"), name="static")

# Dependencia para obtener la sesión de base de datos
def get_db():
    # Se crea nueva sesión de base de datos
    db = SessionLocal()
    try:
        # 'yield' devuelve la sesión para que se use en el request actual
        yield db
    finally:
        # Cerrar la sesión de base de datos al terminar el request
        db.close()

@availableApartmentTableRouter.get("/getAvailableDepartments")
async def get_department(request: Request, db: Session = Depends(get_db)):
    apartamentosdispo = db.query(Apartamento.num_apto, Apartamento.piso_apto, Apartamento.torre_apto).filter(Apartamento.estado_apto == 'disponible').all()
    
    # Si no se encuentran apartamentos
    if not apartamentosdispo:
        return templates.TemplateResponse("apartamentos.html", {"request": request, "error": "No se encontraron apartamentos", "active_page": request.url.path})
    
    # Retornar los apartamentos encontrados a la plantilla
    return templates.TemplateResponse("apartamentos.html", {"request": request, "apartamentosdispo": apartamentosdispo, "active_page": "/templateUsersTable"})