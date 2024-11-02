from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de URL de conexión
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/turesidenciapp"

# Motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})

# Clase base para los modelos
Base = declarative_base()

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
