# Sayulita Web

Este proyecto solo muestra gráficamente las estadísticas generadas por el
proyecto de [Sayulita MIS](https://github.com/AngelGus79/MIS).

# Dependencias

- Python 2.7
- Pip
- Node & NPM 2.0 o superior

# Configurar los settings

Se deben generar las llaves para acceso a las APIs utilizadas:

- [Twitter](https://apps.twitter.com/)
- [Mashape Text Processing](https://market.mashape.com/japerk/text-processing)

Colocar las llaves en el settings.py de django:

``` python
# Llaves de acceso a twitter
TWITTER_APP_KEY = ''
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# Llaves de acceso a Mashape
MASHAPE_KEY = ''
```

# Instalación

``` sh
$ git clone git@github.com:AngelGus79/MIS.git
$ cd ejemplo-django
$ pip install -r requirements.txt
$ cd static && npm install
$ python manage.py runserver
```

Ya con esto se puede visualizar en `http://localhost:8000`, lo que tarde en
cargar los datos es proporcional al número de tweets que se buscan, actualmente
esta en 100.
