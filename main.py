from .modules.menu_file import *
from .modules.resources.mensajes import *

if __name__ == '__main__':

    program = True
    while program:
        """Entrada del programa"""
        print(inicio)
        option = int(input('> '))

        if (option == 1):
            """Ventas"""
            ventas()

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

            elif (option.lower() == 'n'):
                print('De acuerdo!!')
                continue

            else:
                print('\nElija una opción valida')

        else:
            print('\nElija una opción valida')
