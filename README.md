# Filtro Python S2 DuranAlexi

### Resumen


La panadería PanCamp desea implementar un sistema integral de gestión que permita manejar todas las operaciones relacionadas con la administración de productos, proveedores, empleados, clientes, así como la generación de informes relevantes.



## Especificaciones (Funcionalidades):
Para ello, usted es contratado para liderar el desarrollo del sistema que debe cumplir con las siguientes especificaciones:



**Gestión de Ventas y Compras**


**Ventas**: El sistema debe permitir registrar cada transacción de venta con la siguiente información:

- Fecha de la venta.
- Información del cliente (nombre, dirección).
- Información del empleado que realizó la venta (nombre, cargo).
- Productos vendidos (nombre, cantidad, precio).

**Compras:** El sistema debe permitir registrar cada compra realizada a los proveedores con la siguiente información:

- Fecha de la compra.
- Información del proveedor (nombre, contacto).
- Productos comprados (nombre, cantidad, precio de compra).
- Interacción con Proveedores, Empleados y Clientes
**Proveedores**: Registro y gestión de la información de los proveedores incluyendo:

- Nombre.
- Contacto.
- Dirección.

Empleados: Registro y gestión de la información de los empleados incluyendo:

- Nombre.
- Cargo.
- Fecha de contratación.

**Clientes**: Registro y gestión de la información de los clientes incluyendo:

- Nombre.
- Dirección.
- Teléfonos de contacto.

Generación de Informes

**Informes de ventas:** Listado de todas las ventas realizadas en un período de tiempo específico, incluyendo detalles de los productos vendidos y el total de ingresos.

**Informes de stock:** Listado de todos los productos con su cantidad en stock para gestionar de manera proactiva los inventarios.

A continuación se muestra una propuesta para los archivos JSON a construir:



### Productos

```json
JSON propuesto
{
    "Panaderia": {
        "Pan de Bono": 700,
        "Pan de Queso": 800,
        "Pan Cascarita": 500,
        "Pan de Yuca": 800,
        "Calentano": 700,
        "Rollito de Sal": 900,
        "Pan Integral": 700,
        "Pan relleno de Arequipe": 1150,
        "Pan con Salchicha": 1300,
        "Pan recubierto de Chocolate": 1200
    },
    "Pasteleria": {
        "Pastel de Vainilla": 5000,
        "Pastel de Chocolate": 5500,
        "Pastel de bodas": 10000,
        "Glaseado de Vainilla": 3000,
        "Glaseado de Chocolate": 3500,
        "Pastel de Arequipe": 5700,
        "Pastel de Oreo": 7000,
        "Postre de Limon": 4300,
        "Postre de Vainilla": 4000,
        "Postre de Tres Leches": 4500
    },
    "Bebidas": {
        "Coca-Cola": 3000,
        "Pepsi": 2900,
        "Red-Bull": 4000,
        "Gatorade": 3700,
        "Budweiser": 3200,
        "Hit": 2500,
        "Pony-Malta": 2300,
        "Sprite": 3200,
        "Monster": 3000,
        "Tropicana": 2400,
        "-Promociones-": "Algunas promociones de la seccion de Bebidas",
        "1 Pan con Salchicha y 1 Pony Malta": 3000,
        "1 Postre de Oreo y 1 Budweiser": 9000
    },
    "Apartado de promociones": {
        "6 Panes Integrales": 4000,
        "5 Panes recubiertos de Chocolate": 5500,
        "3 Pasteles de Vainilla": 13000,
        "4 Postres de Oreo": 25000,
        "1 Pan con Salchicha y 1 Pony Malta": 3000,
        "1 Postre de Oreo y 1 Budweiser": 9000
    }
}
```


## Resultado esperado

La entrega de este examen debe ser un enlace a un repositorio en GitHub llamado (Examen_Python_ApellidoNombre) que contenga el código de la aplicación construida en Python. En este mismo repositorio, debe contener los siguientes archivos:

- Archivo principal de ejecución basado en Python.
- Archivos modularizados que den funcionalidad al programa principal de Python.
- Archivo JSON que almacene la información del programa en sí.





