from typing import Union
from fastapi import FastAPI

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
@app.get('/pets/read')
def read_pet():
    return {

    }