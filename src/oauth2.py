from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

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
    user = fake_decode_token
    return user

@app.get('/users/me')
async def read_users_me(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}