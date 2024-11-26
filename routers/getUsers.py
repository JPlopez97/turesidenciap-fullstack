from fastapi import Depends, Request, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario, Rol, Residente, Apartamento
from fastapi.templating import Jinja2Templates
from middlewares.verify_token_route import token_required

# Configuración de Jinja2 para trabajar con templates HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router protegido con verificación de token
getUsersRouter = APIRouter(
    tags=["getUsers"],
    responses={404: {"message": "No encontrado"}}
)

@getUsersRouter.get("/templateUsersTable")
async def templateUsersTable(request: Request, db: Session = Depends(get_db)):
    usuarios = db.query(Usuario.cc_usuario, Usuario.nombre_usu, Usuario.correo_electronico, Usuario.telefono, Rol.nombre_rol).join(Rol, Usuario.id_rol == Rol.id_rol).filter(Usuario.id_rol == Rol.id_rol).all()
    
    return templates.TemplateResponse("usuarios.html", {
        "request": request,
        "usuarios": usuarios,
        "active_page": request.url.path
    })

@getUsersRouter.delete("/deleteUser")
async def delete_user(
    cc_usuario: int,
    db: Session = Depends(get_db)
):
    # Buscar el residente por cc_usuario
    residente = db.query(Residente).filter(Residente.cc_usuario == cc_usuario).first()
    
    # Si el residente existe y tiene un apartamento asignado
    if residente and residente.id_apto:
        # Actualizar el estado del apartamento a 'disponible'
        db.query(Apartamento).filter(Apartamento.id_apto == residente.id_apto).update({Apartamento.estado_apto: 'disponible'})
    
    # Eliminar el residente (si existe)
    db.query(Residente).filter(Residente.cc_usuario == cc_usuario).delete()
    
    # Eliminar el usuario
    db.query(Usuario).filter(Usuario.cc_usuario == cc_usuario).delete()

    # Guardar cambios en la base de datos
    db.commit()

    # Redirigir a la tabla de usuarios
    return {"successDelete": "Usuario eliminado exitosamente"}
