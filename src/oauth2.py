import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schema import Usuario, DoesNotExist
from main import verifica_senha

app = FastAPI()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
# Armazenar no os env dps
JWT_SECRET_KEY =  'efdsdssd'  # should be kept secret
JWT_REFRESH_SECRET_KEY = '3fdfs'    # should be kept secret

# Gerando tokens
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt

@app.post('/login', summary="Create access and refresh tokens for user")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        usuario = Usuario.get(login = form_data.username)

        if verifica_senha(bytes(form_data.password, 'utf-8'), bytes(usuario.senha, 'utf-8')):
        # Retorna o token
            return {
                "access_token": create_access_token(usuario.login),
                "refresh_token": create_refresh_token(usuario.login),
            }

    except DoesNotExist:
        return "Login ou senha incorreto(s)!"
    