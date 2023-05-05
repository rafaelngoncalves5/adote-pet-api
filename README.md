# Adote um pet API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Insomnia](https://img.shields.io/badge/Insomnia-black?style=for-the-badge&logo=insomnia&logoColor=5849BE)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

API REST para utilização com app React Native usando [PostgreSQL](https://www.postgresql.org/), [FastAPI](https://fastapi.tiangolo.com/) e [Peewee ORM](https://docs.peewee-orm.com/en/latest/index.html)

## Endpoints



## Autenticação

A autenticação foi feita utilizando [OAuth2](https://oauth.net/2/) e [JWT](https://jwt.io/)

<details>
  <summary>O cliclo de autenticação segue:</summary>
  
  <br />
  
  1 - Usuário cadastra-se no sistema
  
  2 - Usuário faz login com username e password
  
  ![loginendpoint](https://github.com/rafaelngoncalves5/adote-pet-api/blob/login/logout/docs/auth-steps/e1.PNG)
  
  2.1 - Em caso de erro, é emitido um erro com status **403** do HTTP
  
  ![error403](https://github.com/rafaelngoncalves5/adote-pet-api/blob/login/logout/docs/auth-steps/e2.PNG)
  
  3 - Caso os dados estejam corretos, é gerado um ***JWT*** access token e um refresh token
  
  ![tokens](https://github.com/rafaelngoncalves5/adote-pet-api/blob/login/logout/docs/auth-steps/e3.PNG)
  
  4 - Usuário autentica com o **authorize** na API com as credenciais utilizadas na geração do token
  
  ![autoriza](https://github.com/rafaelngoncalves5/adote-pet-api/blob/login/logout/docs/auth-steps/e4.PNG)
  
  > O passo 4 pode e deve ser feito automaticamente
  
  5 - Usuário tem garantido o acesso a um recurso antes inacessível
  
 ![recurso](https://github.com/rafaelngoncalves5/adote-pet-api/blob/login/logout/docs/auth-steps/e5.PNG)
  
</details>
