class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre            # Nombre del producto
        self.cantidad = cantidad        # Cantidad disponible en inventario
        self.precio = precio            # Precio del producto

    # Métodos para obtener y establecer los atributos
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
import json

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def añadir_producto(self, producto):
        if producto.obtener_id() in self.productos:
            print(f"El producto con ID {producto.obtener_id()} ya existe.")
        else:
            self.productos[producto.obtener_id()] = producto
            print(f"Producto {producto.obtener_nombre()} añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado con éxito.")
        else:
            print(f"El producto con ID {id_producto} no se encontró.")

    def actualizar_cantidad(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_cantidad(cantidad)
            print(f"Cantidad actualizada para el producto ID {id_producto}.")
        else:
            print(f"El producto con ID {id_producto} no se encontró.")

    def actualizar_precio(self, id_producto, precio):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_precio(precio)
            print(f"Precio actualizado para el producto ID {id_producto}.")
        else:
            print(f"El producto con ID {id_producto} no se encontró.")

    def buscar_producto(self, nombre):
        productos_encontrados = [prod for prod in self.productos.values() if prod.obtener_nombre() == nombre]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontró ningún producto con el nombre {nombre}.")
        return productos_encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id_producto: prod.__dict__ for id_producto, prod in self.productos.items()}, f)
            print(f"Inventario guardado en {archivo}.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for id_producto, atributos in data.items():
                    producto = Producto(id_producto, atributos['nombre'], atributos['cantidad'], atributos['precio'])
                    self.añadir_producto(producto)
            print(f"Inventario cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {archivo}.")


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
