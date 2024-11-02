from fastapi import FastAPI, Request
from routers import auth_users, busyApartmentTable, getResidentAvailableApartments, register_user, register_apartment, getUsers, availableApartmentTable, routes_html, sendEmail, sendWhatsapp, sendWhatsappResi
from fastapi.templating import Jinja2Templates  # Para trabajar con plantillas HTML mediante Jinja2
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

app.include_router(auth_users.router)
app.include_router(register_user.router)
app.include_router(busyApartmentTable.router)
app.include_router(getResidentAvailableApartments.router)
app.include_router(register_apartment.router)
app.include_router(getUsers.router)
app.include_router(availableApartmentTable.router)
app.include_router(routes_html.router)
app.include_router(sendEmail.router)
app.include_router(sendWhatsapp.router)
app.include_router(sendWhatsappResi.router)
app.mount("/static", StaticFiles(directory="static"), name="static")