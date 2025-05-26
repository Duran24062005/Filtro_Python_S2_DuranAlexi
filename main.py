from src.modules import gestion_ventas
from src.recursos.mensajes import *
from src.auxFunctions.insertion import *
import json

def pancamp_app():

    program = True
    while program:
        """Entrada del programa"""
        print(inicio)
        option = int(input('> '))

        if (option == 1):
            """Ventas"""
            gestion_ventas.ventas()
            continue

        elif (option == 2):
            """Compras"""
            print(json.dumps(abrirJSON(), indent=4, ensure_ascii=False))
            continue

        elif (option == 3):
            """Proveedores"""
            pass

        elif (option == 4):
            """Empleados"""
            pass

        elif (option == 5):
            """Clientes"""
            pass

        elif (option == 6):
            """Informes de ventas"""
            pass

        elif (option == 7):
            """Informes de stock"""
            pass

        elif (option == 8):
            print(finish_program_message)
            salida_opt = input('> ')
            if (salida_opt.lower() == 's'):
                print('Gracias, no vemos pronto!!')
                program = False
                break

            elif (salida_opt.lower() == 'n'):
                print('De acuerdo!!')
                continue

            else:
                print('\nElija una opción valida')

        else:
            print('\nElija una opción valida')


if __name__ == '__main__':
    pancamp_app()