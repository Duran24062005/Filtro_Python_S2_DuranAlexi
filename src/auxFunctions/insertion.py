import json


def abrirJSON():
    dictTemporal = []
    dictTemporal.append
    with open('./db/db_pancamp.json', 'r') as datos:
        dictTemporal = json.load(datos)
    return dictTemporal
    

def guardarDatos(dict, eleption):
    datos = abrirJSON()
    if (eleption==1):
        datos[0]['ventas'].append(dict)
        with open('./db/db_pancamp.json', 'w') as content:
            json.dump(datos, content, indent=4, ensure_ascii=False)
        return True
    
    if (eleption==2):
        return datos[0]['productos']
