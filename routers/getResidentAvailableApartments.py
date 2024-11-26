from fastapi import FastAPI, Depends, Request, APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario, Apartamento, Residente
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

getResidentAvailableApartmentsrouter = APIRouter(tags=["register"], responses={404: {"message": "No encontrado"}})

# Configuración de Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@getResidentAvailableApartmentsrouter.get("/templateApartmentsDispo", response_class=HTMLResponse)
async def templateApartmentsDispo(request: Request, db: Session = Depends(get_db)):
    apartamentos = db.query(Apartamento).filter(Apartamento.estado_apto == 'disponible').all()
    residentes = db.query(Residente.cc_usuario, Usuario.nombre_usu).join(Usuario, Residente.cc_usuario == Usuario.cc_usuario).filter(Residente.id_apto == None).all()

    noResidentDispo = False
    noApartDispo = False
    disableButton = False

    if not residentes:
        noResidentDispo = "No se encontraron residentes disponibles"
        disableButton = True
    
    if not apartamentos:
        noApartDispo = "No se encontraron apartamentos disponibles"
        disableButton = True
    
    return templates.TemplateResponse("assign_apartment.html", {
        "request": request,
        "residentes": residentes,
        "apartamentos": apartamentos,
        "noResidentDispo": noResidentDispo,
        "noApartDispo": noApartDispo,
        "disableButton": disableButton, 
        "active_page": request.url.path
    })


@getResidentAvailableApartmentsrouter.post("/assign_apartment", response_class=HTMLResponse)
async def assignApartment(
    cc_usuario: int = Form(...),
    id_apto: int = Form(...),
    db: Session = Depends(get_db)
    ):

    # Realizar la asignación
    db.query(Residente).filter(Residente.cc_usuario == cc_usuario).update({Residente.id_apto: id_apto})
    db.query(Apartamento).filter(Apartamento.id_apto == id_apto).update({Apartamento.estado_apto: 'ocupado'})
    db.commit()

    return RedirectResponse(url="/templateApartmentsDispo?message=Asignación+exitosa", status_code=303)