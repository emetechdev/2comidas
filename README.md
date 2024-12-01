# 2comidas

MVP del proycto 2Comidas. Es una versión Beta

# Requisitos previos

- Tener instalado git
- Tener instalado python

# Descargar el proyecto

1. Crear una carpeta (ejemplo: `"proyecto-2C-carpeta"`)
2. Abrir una terminal (o shell) dentro de la carpeta `"proyecto-2C-carpeta"` y escribir
``` bash
$ git clone https://github.com/emetechdev/2comidas
```
3. Se va a descargar una carpeta llamada`2comidas`. En la terminal (ya abierta) escribir:
``` bash
$ cd 2comidas
```
4. Luego escribir: (crea un entorno virtual para que se ejecute el proyecto)
``` bash
$ python3 -m venv .env
```
5. Luego escribir: (esto instala todas las librerias necesarias para que funcione el proyecto)
``` bash
$ pip install -r requirements.txt
```
6. Luego escribir: (con esto entrás a la carpeta que contiene el proyecto)
``` bash
$ cd doscomidas
```
7. Por ultimo tirar estos 3 comandos. Con *runserver* queda levantado el servidor de django y ya quedaria listo para consumir las apis
``` bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
