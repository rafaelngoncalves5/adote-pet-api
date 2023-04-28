from peewee import *
from datetime import datetime

psql_db = PostgresqlDatabase('mydb', user='postgres', password='birdscooter123')

# Conectando ao psql_db
psql_db.connect()

class BaseModel(Model):
    class Meta:
        database = psql_db

class Usuario(BaseModel):
    id = AutoField(primary_key=True)
    nome_completo = CharField(max_length=150, null=True)
    email = CharField(max_length=150)
    telefone = CharField(max_length=150)
    cpf = CharField(max_length=150, null=True)
    complemento = CharField(max_length=150, null=True)
    cep = CharField(max_length=150, null=True)
    data_de_nascimento = TimestampField()
    login = CharField(max_length=150)
    senha = CharField(max_length=150)
    data_de_criacao = TimestampField(default=datetime.now())

    def __str__(self):
        return str(f"Usuário {self.nome_completo}, com id {self.id}")

class Animal(BaseModel):
    id = AutoField(primary_key=True)
    # Era interessante considerar passar uma tupla 'choices' pra 'tipo' e 'raca'
    tipo = CharField(max_length=150)
    raca = CharField(max_length=150)
    genero = CharField(max_length=150)
    nome_completo = CharField(max_length=150)
    data_de_nascimento = TimestampField()
    flag_castrado = BooleanField(default=False)
    usuario_id = ForeignKeyField(Usuario, backref='usuario')
    data_de_criacao = TimestampField(default=datetime.now())

    def __str__(self):
        return str(f"Animal {self.nome_completo}, da raça {self.raca}, com id {self.id}, de dono {self.usuario_set.nome_completo}")


psql_db.create_tables([Usuario, Animal])