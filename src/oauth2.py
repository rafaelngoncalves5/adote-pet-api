from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from schema import Usuario
from main import verifica_senha

app = FastAPI()

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

# tokenUrl é o endpoint que receberá 'username' e 'password'
# A API checa esses dados e retorna um token
# Quando o frontend requisita algo protegido da API, precisamos passar o token
# Passamos esse token no cabeçalho da requisição, como, Authorization, Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Recebe um token e retorna um usuário
def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
# === Path operations ===

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # Pega o usuário no BD
    usuario = Usuario.get(login = form_data.username)

    # Se o usuário não existir
    if not usuario:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Pega a senha do formulário
    senha = form_data.password

    # Verifica se a senha está correta
    if verifica_senha(bytes(senha, encoding='utf-8'), bytes(usuario.senha, encoding='utf-8')):     
         return {"access_token": usuario.login, "token_type": "bearer"}
            
    else:
        return "Login ou senha incorreto(s)!"

@app.get('/users/me')
async def read_users_me(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}