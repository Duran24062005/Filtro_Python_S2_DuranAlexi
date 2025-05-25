import json


def abrirJSON():
    dictTemporal = []
    with open('../db/db_pancamp.json', 'r') as datos:
        dictTemporal = json.load(datos)
    return dictTemporal
    

def guardarDatos(datos, eleption):
    if (eleption==1):
        return database[0]['products']
    
    if (eleption==1):
        return database[0]['ventas']
