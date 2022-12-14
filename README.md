# Tu-Canchita-API

## Iniciar proyecto en local:

1. Clonar el repositorio
2. Crear el entorno virtual, activarlo, e instalar requirements:

```bash
$ virtualenv venv
$ source venv/Scripts/activate
$ pip3 install -r requirements.txt
```

3. Configurar archivo .env:

```
SECRET_KEY='**********'
DATABASE_URL=postgres://usuariodepostgres:contraseña@127.0.0.1:5432/nombrebd
```

4. Migrar modelos y base de datos:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Crear super usuario:

Escribimos en consola:

```bash
$ python manage.py createsuperuser
```

# ENDPOINTS

## AUTH

### Create User:

POST http://localhost:8000/auth/users/

Body:

```JSON
{
  "email": "email@gmail.com",
  "first_name": "First Name",
  "last_name": "Last Name",
  "password": "Password",
  "re_password": "Password",
  "group": 1
}
```

Response: Status 201 Created

```JSON
{
  "message": "User created successfully",
}
```

### JWT Token Create (login):

http://localhost:8000/auth/jwt/create/

Body:

```JSON
{
  "email": "email@gmail.com",
  "password": "Password"
}
```

Response:

```JSON
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzExMjI5NCwianRpIjoiNjYyNzI4MzIzYWY3NGZiMDhjYzhmNWFjY2ViNTRhY2QiLCJ1c2VyX2lkIjoxfQ._RWDkBbVoWqpwah2KRc87IN--KhmkPJ6pzsVN_GqMP8",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxMTI1MDk0LCJqdGkiOiIxMjU4OGI2NWYwYTk0NjI3OTI4Zjc5MDdkMTdmYjk2MSIsInVzZXJfaWQiOjF9.LtLdFB9I_lV5715Ft9OFi_J05kK_5aN9CkbFVorpzjk"
}
```

### JWT Token Refresh:

http://localhost:8000/auth/jwt/refresh/

Body:

```JSON
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzExMjI5NCwianRpIjoiNjYyNzI4MzIzYWY3NGZiMDhjYzhmNWFjY2ViNTRhY2QiLCJ1c2VyX2lkIjoxfQ._RWDkBbVoWqpwah2KRc87IN--KhmkPJ6pzsVN_GqMP8"
}
```

Response:

```JSON
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxMTI1NDgxLCJqdGkiOiI3NGIxNTZjMjY0ODI0NjBiYTMxOThhZTI5NWFjODQyNSIsInVzZXJfaWQiOjF9.vbtXxdDqt25u1T7ekLvqgKkXzJlwJLAuDpVugJV9e8I"
}
```

### JWT Token Verify:

http://localhost:8000/auth/jwt/verify/

Body

```JSON
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxMTI1NDgxLCJqdGkiOiI3NGIxNTZjMjY0ODI0NjBiYTMxOThhZTI5NWFjODQyNSIsInVzZXJfaWQiOjF9.vbtXxdDqt25u1T7ekLvqgKkXzJlwJLAuDpVugJV9e8I"
}
```

Response: status 200 OK

<!-- ### GET User Info:

http://localhost:8000/auth/users/me/

Headers: Content-Type: JWT "Token Access"

## SPORT

### GET Sports

http://localhost:8000/api/sport/sports

Response:

```JSON
{
  "sports": [
    {
      "id": 1,
      "name": "Fútbol"
    },
    {
      "id": 2,
      "name": "Paddle"
    },
    {
      "id": 3,
      "name": "Tenis"
    },
    {
      "id": 4,
      "name": "Basket"
    }
  ]
}
```

## SERVICE

### GET Services

http://localhost:8000/api/service/services

Response:

```JSON
{
  "services": [
    {
      "id": 1,
      "name": "Estacionamiento"
    },
    {
      "id": 2,
      "name": "Asador"
    },
    {
      "id": 3,
      "name": "Vestuarios"
    },
    {
      "id": 4,
      "name": "Baños"
    },
    {
      "id": 5,
      "name": "Salón de eventos"
    }
  ]
}
``` -->
