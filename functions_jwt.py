from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
import os

# Clave secreta para firmar los tokens
SECRET_KEY = os.getenv("SECRET_KEY")  # Usa un valor por defecto para desarrollo.

# Función para calcular la fecha de expiración
def expire_date(days: int):
    return datetime.now() + timedelta(days)

# Generar un token JWT
def write_token(data: dict):
    try:
        token = encode(
            payload={**data, "exp": expire_date(1)},  # Agregar fecha de expiración
            key=SECRET_KEY,
            algorithm="HS256"
        )
        return token
    except Exception as e:
        return JSONResponse(content={"message": f"Error al generar el token: {str(e)}"}, status_code=500)

# Validar un token JWT
def validate_token(token: str, output: bool = False):
    try:
        payload = decode(token, key=SECRET_KEY, algorithms=["HS256"])
        if output:
            return payload  # Retorna el contenido del token si es necesario
        return payload if output else True
    except exceptions.DecodeError:
        raise JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        raise JSONResponse(content={"message": "Token Expired"}, status_code=401)
