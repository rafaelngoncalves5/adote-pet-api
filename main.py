from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime

from schema import Animal, Usuario

genero_tuple = ('Masculino', 'Feminino', 'Outro')

class PyAnimal(BaseModel):
    tipo: str
    raca: str
    genero: str
    nome_completo: str
    data_de_nascimento: date | None
    flag_castrado: bool
    usuario_id: int

app = FastAPI()

@app.get("/")
def read_home():
    welcome_msg = "Bem vindo ao adote seu pet! 🐶"
    intro_msg = "Os endpoints disponiíveis são:"
    home_url = "/"
    read_pet_url = "/pet/read",
    detail_pet_url = "/pet/{id}/details",
    create_pet_url = "/pet/create",
    update_pet_url = "/pet/update",
    delete_pet_url = "/delete_pet",

    return {
        "Bem vindo": welcome_msg,
        "Introdução": intro_msg,
        "Home (GET)": home_url,
        "Listagem de pets (GET)": read_pet_url,
        "Detalhes (GET)": detail_pet_url,
        "Criação de pets (GET/POST)": create_pet_url,
        "Alteração de pets (GET/PUT)": update_pet_url,
        "Exclusão de pets (GET/DELETE): ": delete_pet_url,
        # ...
        }

# Detalhes
@app.get('/pet/{id}/details')
def detail_pet(id: int):
    animal = Animal.get(id = id)
    
    return {
        "Id": animal.id,
        "Tipo": animal.tipo,
        "Raça": animal.raca,
        "Gênero": animal.genero,
        "Nome completo": animal.nome_completo,
        "Data de nascimento": animal.data_de_nascimento,
        "Castrado": animal.flag_castrado,
        "Dono": animal.usuario_id,
        "Data de criação": animal.data_de_criacao   
    }

# === CRUD de animais ===
    
# Create
@app.get('/pet/create')
def create_pet_get():
    return {
        "Bem vindo": "Bem vindo a URL para criação de pets. Para criar um pet, envie um JSON, com o seguintes dados: ",
        "tipo": "Tipo do animal (string)",
        "raca": "Raça do animal (string)",
        "genero": "Masculino, Feminino ou Outro (enum/string/tuple)",
        "nome_completo": "Nome completo do animal (string)",
        "data_de_nascimento": "Data de nascimento do animal (string/date). Envie uma string no seguinte formato: YY-MM-DD. Por exemplo: 2020-04-20",
        "flag_castrado": "O animal foi castrado (boolean)?",
        "usuario_id": "A qual usuário este animal pertence"
        }

@app.post('/pet/create')
def create_pet(animal: PyAnimal):
    try:
        new_animal = Animal.create(
            tipo=animal.tipo,
            raca=animal.raca,
            genero=animal.genero,
            nome_completo=animal.genero,
            data_de_nascimento=animal.data_de_nascimento,
            flag_castrado=animal.flag_castrado,
            usuario_id=animal.usuario_id,
        )
        return {"Animal {} criado com sucesso!".format(new_animal)}
    
    except TypeError:
        return {"erro": TypeError, "msg": "Por favor, verifique os dados enviados. Leia nosso /pet/read (GET)!"}
    except ValueError:
        return {"erro": TypeError, "msg": "Por favor, verifique os dados enviados. Leia nosso /pet/read (GET)!"}

# Read
@app.get('/pet/read')
def read_pet():
    my_list = list()
    for animal in Animal.select():
        my_list.append({
            animal.id: {
                "Id": animal.id,
                "Nome completo": animal.nome_completo,
                "Tipo": animal.tipo,
                "Raça": animal.raca,
                "Gênero": animal.genero,
                "Data de nascimento": animal.data_de_nascimento,
                "Dono: ": animal.usuario_id,
                "Data de criação": animal.data_de_criacao,
            },
        })
    return my_list


# print(schema.shaolin_pig_killer)
# print(schema.baby_eater)