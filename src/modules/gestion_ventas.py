from ..recursos.mensajes import *
from ..auxFunctions.insertion import *
from datetime import datetime
from tabulate import tabulate




def ventas():
    nombre_v = input('Diga, su nombre: ')
    cargo = input('Diga, su cargo: ')
    print('\n============================================\n')
    nombre_cliente = input('Diga el nombre del cliente: ')
    client_address = input('Diga la dirección del cliente: ')
    print('\n============================================\n')
    nombre_product = input('Diga el nombre del producto: ')
    cant_product = int(input('Diga la cantidad: '))
    unit_price = int(input('Precio unitario: '))

    print(
        register_user(
            nombre_v, cargo, nombre_cliente, 
            client_address , nombre_product, 
            cant_product, unit_price))


def calcular_valor_total(unidades, valor_unidad):
    return valor_unidad*unidades
    

def register_user(
        name, cargo, name_client, 
        client_address, product_name, 
        product_cant, unit_price
        ):

    valor_total = calcular_valor_total(product_cant, unit_price)
    hoy = datetime.now().strftime('%Y-%m-%d')
    
    new_venta = {
        "fecha": hoy,
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
            "Valor total venta": valor_total
        }
    }

    data = [
        ["Fecha", hoy],
        ["Vendedor", name],
        ["Cargo", cargo],
        ["Cliente", name_client],
        ["Dirección Cliente", client_address],
        ["Producto", product_name],
        ["Cantidad", product_cant],
        ["Precio Unidad", unit_price],
        ["Valor Total Venta", valor_total]
    ]
    print(tabulate(data, headers=['Campo', 'Valor'], tablefmt='rounded_grid'))