# MIS

Proyecto del curso propedéutico para ingresar a la MIS. Consiste en:

- Determinar cuantos hombres y cuantas mujeres hablan de sayulita.
- Determinar el sentimiento de la gente que visita sayulita.

El proyecto consiste en una librería que puede importarse en un proyecto que
quiera hacer algo con los datos devueltos, como ejemplo se hizo un proyecto
básico de django que utiliza la librería para presentar los datos visualmente.

## Dependencias

- Python 2.7
- Pip


Se deben generar las llaves para acceso a las APIs utilizadas:

- [Twitter](https://apps.twitter.com/)
- [Mashape Text Processing](https://market.mashape.com/japerk/text-processing)

Colocar las llaves en el archivo `src/settings.py`

## Instalación

``` sh
$ git clone git@github.com:AngelGus79/MIS.git
$ pip install twython mock requests httpretty
```

## Ejemplos de uso

Pueden verse en la carpeta `test/` o bien en el `ejemplo-django/` que contiene
las instrucciones de instalación en [ejemplo-django/README.md](ejemplo-django/README.md)

## Ejecución de los tests

Una vez se tenga la librería instalada, se puede usar el script
[`run_tests.sh`](run_tests.sh).

``` sh
$ ./run_tests.sh
```
