from fastapi import FastAPI, Depends, Request, APIRouter
from fastapi.responses import HTMLResponse  # Para devolver respuestas HTML
from sqlalchemy.orm import Session  # Manejo de sesiones con SQLAlchemy
from database import SessionLocal  # Sesión de base de datos configurada
from models import Usuario, Apartamento, Residente  # Modelos de la base de datos
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML mediante Jinja2
from fastapi.staticfiles import StaticFiles # Para trabajar con los css, js, img, etc.


router = APIRouter(tags=["getDepartments"], 
                   responses={404: {"message": "No encontrado"}})

# Configuración Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

router.mount("/static", StaticFiles(directory="static"), name="static")

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

# Ruta para mostrar el template
@router.get("/templateDepartments", response_class=HTMLResponse)
async def template_ndex(request: Request):
    return templates.TemplateResponse("residentes.html", {"request": request})


@router.get("/getBusyDepartments")
async def get_department(request: Request, db: Session = Depends(get_db)):
    apartamentos = db.query(Apartamento.id_apto, Apartamento.num_apto, Apartamento.torre_apto, Residente.cc_usuario, Usuario.nombre_usu)\
    .join(Residente, Apartamento.id_apto == Residente.id_apto).join(Usuario, Residente.cc_usuario == Usuario.cc_usuario).all()
    
    # Si no se encuentran apartamentos o residentes
    if not apartamentos:
        return templates.TemplateResponse("residentes.html", {"request": request, "error": "No se encontraron usuarios"})
    
    # Retornar los apartamentos encontrados a la plantilla
    return templates.TemplateResponse("residentes.html", {"request": request, "apartamentos": apartamentos})

@router.post("/releaseApartment")
async def releaseApartment(
    id_apto: int,
    db: Session = Depends(get_db)):
   
   apartamento = db.query(Apartamento).filter(Apartamento.id_apto == id_apto).first()

   if apartamento and apartamento.estado_apto == 'ocupado':
       db.query(Apartamento).filter(Apartamento.id_apto == apartamento.id_apto).update({Apartamento.estado_apto: 'disponible'})
       db.query(Residente).filter(Residente.id_apto == apartamento.id_apto).update({Residente.id_apto: None})
       db.commit()

   return {"message": "Apartamento liberado con éxito"}
