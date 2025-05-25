from resources.mensajes import *
from functions.insertion import *
from tabulate import tabulate

def calcular_valor_total(unidades, valor_unidad):
    return valor_unidad*unidades
    

def register_user(
        name, cargo, name_client, 
        client_address, date,
        product_name, product_cant,
        unit_price
        ):
    
    new_venta = {
        "fecha": date,
        "vendedor": {
            "Nombre": name,
            "Cargo": cargo
        },
        "cliente": {
            "Nombre": name_client,
            "Dirreción": client_address
        },
        "productos": {
            "Nombre": product_name,
            "Cantidad": product_cant,
            "Precio unidad": unit_price,
            "Valor total venta": calcular_valor_total(product_cant, unit_price)
        }
    }
    print(tabulate(new_venta, headers='keys', tablefmt='rounded_grid'))