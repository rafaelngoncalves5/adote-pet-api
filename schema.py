from peewee import *

psql_db = PostgresqlDatabase('mydb', user='postgres', password='birdscooter123')

# Conectando ao psql_db
psql_db.connect()

class BaseModel(Model):
    class Meta:
        database = psql_db

class User(BaseModel):
    username = CharField
