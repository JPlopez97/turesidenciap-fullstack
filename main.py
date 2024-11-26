from fastapi import FastAPI, Request
from routers import sendEmail
from routers.auth_users import auth_router
from routers.register_user import register_user_router
from routers.busyApartmentTable import busyApartmentTableRouter
from routers.getResidentAvailableApartments import getResidentAvailableApartmentsrouter
from routers.register_apartment import registerApartmentRouter
from routers.getUsers import getUsersRouter
from routers.availableApartmentTable import availableApartmentTableRouter
from routers.routes_html import htmlRoutes
from routers.sendWhatsapp import sendWhatsappRouter
from routers.sendWhatsappResi import sendWhatsappResiRouter
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML mediante Jinja2
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Incluir rutas con validación de token
app.include_router(auth_router)  # Esta ruta ahora tiene protección por token
app.include_router(register_user_router)
app.include_router(busyApartmentTableRouter)
app.include_router(getResidentAvailableApartmentsrouter)
app.include_router(registerApartmentRouter)
app.include_router(getUsersRouter)
app.include_router(availableApartmentTableRouter)
app.include_router(htmlRoutes)
app.include_router(sendEmail.router)
app.include_router(sendWhatsappRouter)
app.include_router(sendWhatsappResiRouter)

# Rutas estáticas
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar variables de entorno
load_dotenv()