class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_atributos(self):
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe.")
        else:
            self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(f"El producto con ID {id_producto} no se encontró.")

    def actualizar_cantidad(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_cantidad(cantidad)
        else:
            print(f"El producto con ID {id_producto} no se encontró.")

    def actualizar_precio(self, id_producto, precio):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_precio(precio)
        else:
            print(f"El producto con ID {id_producto} no se encontró.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                print(producto)
                return producto
        print(f"No se encontró ningún producto con el nombre {nombre}.")
        return None

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id_producto: prod.obtener_atributos() for id_producto, prod in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for id_producto, atributos in data.items():
                    self.añadir_producto(Producto(id_producto, atributos['Nombre'], atributos['Cantidad'], atributos['Precio']))
        except FileNotFoundError:
            print("El archivo no se encontró.")


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo('inventario.json')

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Cantidad")
        print("4. Actualizar Precio")
        print("5. Buscar Producto")
        print("6. Mostrar Todos los Productos")
        print("7. Guardar y Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre del Producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del Producto: ")
            cantidad = int(input("Nueva Cantidad: "))
            inventario.actualizar_cantidad(id_producto, cantidad)

        elif opcion == '4':
            id_producto = input("ID del Producto: ")
            precio = float(input("Nuevo Precio: "))
            inventario.actualizar_precio(id_producto, precio)

        elif opcion == '5':
            nombre = input("Nombre del Producto: ")
            inventario.buscar_producto(nombre)

        elif opcion == '6':
            inventario.mostrar_todos()

        elif opcion == '7':
            inventario.guardar_en_archivo('inventario.json')
            print("Inventario guardado. Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
