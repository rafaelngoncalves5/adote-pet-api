import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import JWTError, jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import ValidationError
from schema import Usuario, DoesNotExist
from main import verifica_senha
from typing import Annotated

app = FastAPI()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
# Armazenar no os env dps
JWT_SECRET_KEY =  'efdsdssd'  # should be kept secret
JWT_REFRESH_SECRET_KEY = '3fdfs'    # should be kept secret

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="user/login",
    scheme_name="JWT"
)

# Parte 1 - Gerando tokens
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

# Parte 2 - Login
@app.post('user/login', summary="Recebe um username e password e retorna um token de acesso e um de refresh")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        usuario = Usuario.get(login = form_data.username)

        if verifica_senha(bytes(form_data.password, 'utf-8'), bytes(usuario.senha, 'utf-8')):
            # Retorna o token
            return {
                "access_token": create_access_token(usuario.login),
                "refresh_token": create_refresh_token(usuario.login),
                }
        else:
            return "Login ou senha incorreto(s)!"

    except DoesNotExist:
        return "Login ou senha incorreto(s)!"

# Parte 3 - Rotas protegidas
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = payload
        
        if datetime.fromtimestamp(token_data['exp']) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expirou",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Credenciais não puderam ser validadas {}".format(token_data),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except DoesNotExist:
        return "Login ou senha incorreto(s)!"
        
    usuario = Usuario.get(login = token_data['sub'])

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return usuario

'''@app.get('/me')
async def get_me(user: Usuario = Depends(get_current_user)):
    return user'''