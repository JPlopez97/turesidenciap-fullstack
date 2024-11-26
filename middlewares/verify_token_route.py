from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from functions_jwt import validate_token

security = HTTPBearer()


# Dependencia para proteger rutas
def token_required(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = validate_token(token)
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
