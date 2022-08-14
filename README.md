# Tu-Canchita-API

## Iniciar proyecto en local:

1. Clonar el repositorio
2. Crear el entorno virtual, activarlo, e instalar requirements:

```bash
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

3. Configurar archivo .env:

```Python
SECRET_KEY='**********'
DATABASE_URL=postgres://usuariodepostgres:contraseña@127.0.0.1:5432/nombrebd
```

## Crear super usuario:

Escribimos en consola:

```bash
$ python manage.py createsuperuser
```
