import json
from db.db_pancamp import database


def abrirJSON():
    dictTemporal = []
    with open('./db/db_pancamp.json', 'r') as datos:
        print(json.decoder(datos))
    return dictTemporal

def guardarDatos(datos, eleption):
    if (eleption==1):
        return database[0]['products']
    
    if (eleption==1):
        return database[0]['ventas']
