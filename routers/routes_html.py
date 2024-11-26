from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

htmlRoutes = APIRouter(tags=["templates"], responses={404: {"message": "No encontrado"}})

templates = Jinja2Templates(directory="templates")

@htmlRoutes.get("/templateQuienesSomosTuResidenciApp")
async def templateIndexAdmin(request: Request):
    return templates.TemplateResponse("quienesSomosTuResidenciApp.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateIndexAdmin")
async def templateIndexAdmin(request: Request):
    return templates.TemplateResponse("indexAdmin.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateIndexResidente")
async def templateIndexResidente(request: Request):
    return templates.TemplateResponse("indexResidente.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateAdministracion")
async def templateAdministracion(request: Request):
    return templates.TemplateResponse("administracion.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateContacto")
async def templateContacto(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateContactoResi")
async def templateContactoResi(request: Request):
    return templates.TemplateResponse("contactoResi.html", {"request": request, "active_page": request.url.path})

# @router.get("/templateNotificaciones")
# async def templateNotificaciones(request: Request):
#     return templates.TemplateResponse("notificaciones.html", {"request": request})

@htmlRoutes.get("/templateNotificacionesResi")
async def templateNotificacionesResi(request: Request):
    return templates.TemplateResponse("notificacionesResidentes.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateNosotros")
async def templateNosotros(request: Request):
    return templates.TemplateResponse("quienessomos.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateNosotrosResi")
async def templateNosotrosResi(request: Request):
    return templates.TemplateResponse("quienessomosResi.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateReservas")
async def templateReservas(request: Request):
    return templates.TemplateResponse("Reservas.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateReservasResi")
async def templateReservasResi(request: Request):
    return templates.TemplateResponse("ReservasResi.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templatePagos")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("pagos.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templatePoliticaDatos")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("politicaDatos.html", {"request": request, "active_page": request.url.path})

# Templates Propietario (de momento)
@htmlRoutes.get("/templateIndexadminPro")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("indexAdminpro.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateAdministracionpro")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("administracionpro.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateReservaspro")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("Reservaspro.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateNotificacionespro")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("notificacionespro.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateContactopro")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("contactopro.html", {"request": request, "active_page": request.url.path})

@htmlRoutes.get("/templateNosotrospro")
async def template_Pagos(request: Request):
    return templates.TemplateResponse("quienessomospro.html", {"request": request, "active_page": request.url.path})

#Copie y pegue el mismo que tiene el residente cucho