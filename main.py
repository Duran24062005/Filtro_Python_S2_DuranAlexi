from src.modules import gestion_ventas
from src.recursos.mensajes import *

def pancamp_app():

    program = True
    while program:
        """Entrada del programa"""
        print(inicio)
        option = int(input('> '))

        if (option == 1):
            """Ventas"""
            gestion_ventas.ventas()

        elif (option == 2):
            """Compras"""
            pass

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

            elif (salida_opt.lower() == 'n'):
                print('De acuerdo!!')
                continue

            else:
                print('\nElija una opción valida')

        else:
            print('\nElija una opción valida')


if __name__ == '__main__':
    pancamp_app()