from resources.mensajes import *
from functions.insertion import *
from functions.functionsList import *




def ventas():
    nombre_v = input('Diga, su nombre: ')
    cargo = input('Diga, su cargo: ')
    print('\n============================================\n')
    nombre_cliente = input('Diga el nombre del cliente: ')
    client_address = input('Diga la dirección del cliente: ')
    print('Formato fecha: AAAA-MM-DD')
    venta_date = input('Fecha de la venta: ')
    print('\n============================================\n')
    nombre_product = input('Diga el nombre del producto: ')
    cant_product = int(input('Diga la cantidad: '))
    unit_price = int(input('Precio unitario: '))

    print(
        register_user(
            nombre_v, cargo, nombre_cliente, 
            client_address , venta_date, 
            nombre_product, cant_product, unit_price))

def auth_user(user):
    pass


def finish_program():
    print('Gracias, no vemos pronto!!')