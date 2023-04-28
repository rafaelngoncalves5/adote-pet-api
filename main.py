from typing import Union
from fastapi import FastAPI

from schema import Animal, Usuario

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
        "Criação de pets (POST)": create_pet_url,
        "Alteração de pets (PUT)": update_pet_url,
        "Exclusão de pets (DELETE): ": delete_pet_url,
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
@app.post('/pet/create')
def create_pet():
    pass

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