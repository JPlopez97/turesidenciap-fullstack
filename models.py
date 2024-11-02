from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Modelo de Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    cc_usuario = Column(Integer, primary_key=True)
    nombre_usu = Column(String(100), nullable=False)
    correo_electronico = Column(String(50), nullable=False, unique=True)
    telefono = Column(String(15), nullable=False, unique=True)
    contrasena = Column(String(255), nullable=False)
    id_rol = Column(Integer, ForeignKey('roles.id_rol'))

    rol = relationship("Rol", back_populates="usuarios")

# Modelo de Rol
class Rol(Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True)
    nombre_rol = Column(String(50), nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")

# Modelo de Apartamento
class Apartamento(Base):
    __tablename__ = 'apartamentos'
    id_apto = Column(Integer, primary_key=True, index=True)
    num_apto = Column(Integer, nullable=False)
    piso_apto = Column(Integer, nullable=False)
    torre_apto = Column(Integer, nullable=False)
    estado_apto = Column(String(20))
    fecha_creacion = Column(DateTime, default=datetime.now)
    fecha_final = Column(DateTime)
    
    # Relación con Residente (especificando foreign_keys)
    residente = relationship("Residente", foreign_keys="[Residente.id_apto]", back_populates="apartamento")

class Residente(Base):
    __tablename__ = 'residentes'
    cc_usuario = Column(Integer, primary_key=True, nullable=False)
    id_apto = Column(Integer, ForeignKey('apartamentos.id_apto'), unique=True, nullable=True)

    # Relación con Apartamento
    apartamento = relationship("Apartamento", foreign_keys=[id_apto], back_populates="residente")
