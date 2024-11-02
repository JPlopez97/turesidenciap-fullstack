from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["templates"], responses={404: {"message": "No encontrado"}})

templates = Jinja2Templates(directory="templates")

@router.get("/templateIndexAdmin")
async def templateIndexAdmin(request: Request):
    return templates.TemplateResponse("indexAdmin.html", {"request": request})

@router.get("/templateIndexResidente")
async def templateIndexResidente(request: Request):
    return templates.TemplateResponse("indexResidente.html", {"request": request})

@router.get("/templateAdministracion")
async def templateAdministracion(request: Request):
    return templates.TemplateResponse("administracion.html", {"request": request})

@router.get("/templateContacto")
async def templateContacto(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request})

@router.get("/templateContactoResi")
async def templateContactoResi(request: Request):
    return templates.TemplateResponse("contactoResi.html", {"request": request})

# @router.get("/templateNotificaciones")
# async def templateNotificaciones(request: Request):
#     return templates.TemplateResponse("notificaciones.html", {"request": request})

@router.get("/templateNotificacionesResi")
async def templateNotificacionesResi(request: Request):
    return templates.TemplateResponse("notificacionesResidentes.html", {"request": request})

@router.get("/templateNosotros")
async def templateNosotros(request: Request):
    return templates.TemplateResponse("quienessomos.html", {"request": request})

@router.get("/templateNosotrosResi")
async def templateNosotrosResi(request: Request):
    return templates.TemplateResponse("quienessomosResi.html", {"request": request})

@router.get("/templateReservas")
async def templateReservas(request: Request):
    return templates.TemplateResponse("Reservas.html", {"request": request})

@router.get("/templateReservasResi")
async def templateReservasResi(request: Request):
    return templates.TemplateResponse("ReservasResi.html", {"request": request})