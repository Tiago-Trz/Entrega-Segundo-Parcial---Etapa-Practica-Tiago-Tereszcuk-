import json
import os

def cargar_datos():
    # si el archivo existe lo abro y cargo los datos
    if os.path.exists("alumnos.json"):
        with open("alumnos.json", "r") as archivo:
            datos = json.load(archivo)
            return datos
    else:
        # si no existe, arranco con un diccionario vacio
        return {}

def guardar_datos(diccionario_alumnos):
    # abro el json en modo escritura y guardo todo el diccionario
    with open("alumnos.json", "w") as archivo:
        json.dump(diccionario_alumnos, archivo, indent=4)