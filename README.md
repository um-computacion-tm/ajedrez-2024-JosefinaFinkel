# ajedrez-2024-JosefinaFinkel
ajedrez-2024-JosefinaFinkel created bu GitHub Classroom

Proyecto de Ajedrez en Python Orientado a Objetos realizado por Josefina Finkel.
Legajo 63173

## Reglamento
El juego es un ajedrez, sin jaque mate, ni enroque.
La forma de que termine la partida es capturar el rey contrario

## Como ejecutar
El juego no cuenta con interfaz gráfica, por lo que se ejecuta desde la línea de comandos.

## Ejecucion usando Docker
Para ejecutar el juego usando Docker, antes debes instalar Docker en tu computadora.
Una vez instalado Docker, puedes ejecutar el juego con los siguientes comandos:

#### Crear imagen Docker
```
$ sudo docker buildx build -t ajedrez --no-cache .
```
#### Para ejecutar el juego
```
$ sudo docker run -i ajedrez
```

# :books: Documentación
## CHANGELOG
El changelog contiene una lista de las versiones del proyecto, con los cambios, eliminaciones y adiciones realizados en cada versión.


# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-JosefinaFinkel/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-JosefinaFinkel/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/74b7bb313dd37f3bd2bf/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-JosefinaFinkel/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/74b7bb313dd37f3bd2bf/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-JosefinaFinkel/test_coverage)