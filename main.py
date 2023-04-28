from typing import Union
from fastapi import FastAPI

import schema

app = FastAPI()

@app.get("/")
def read_home():
    welcome_msg = "Bem vindo ao adote seu pet! 🐶"
    intro_msg = "Os endpoints disponiíveis são:"
    home_url = "/"
    read_pet_url = "/read_pet",
    create_pet_url = "/create_pet",
    update_pet_url = "/update_pet",
    delete_pet_url = "/delete_pet",

    return {
        "Bem vindo": welcome_msg,
        "Introdução": intro_msg,
        "Home (GET)": home_url,
        "Listagem de pets (GET)": read_pet_url,
        "Criação de pets (POST)": create_pet_url,
        "Alteração de pets (PUT)": update_pet_url,
        "Exclusão de pets (DELETE): ": delete_pet_url,
        # ...
        }

# CRUD de animais
@app.get('/pet/read')
def read_pet():
    my_list = list()
    for animal in schema.Animal.select():
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