from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Motor de la base de datos
engine = create_engine(getenv("DATABASE_URL"), connect_args={"charset": "utf8mb4"})

# Clase base para los modelos
Base = declarative_base()

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
