class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para establecer y obtener atributos
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

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
            print(f"Producto {producto.nombre} añadido al inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre {nombre}.")

    def mostrar_todos_los_productos(self):
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
from inventario import Inventario, Producto

def menu():
    print("---- Sistema de Gestión de Inventario ----")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Guardar Inventario")
    print("7. Cargar Inventario")
    print("8. Salir")
    return input("Selecciona una opción: ")

def main():
    inventario = Inventario()

    while True:
        opcion = menu()

        if opcion == "1":
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre del Producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del Producto a actualizar: ")
            nueva_cantidad = input("Nueva Cantidad (presiona enter para omitir): ")
            nuevo_precio = input("Nuevo Precio (presiona enter para omitir): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del Producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            archivo = input("Nombre del archivo para guardar (con .json): ")
            inventario.guardar_en_archivo(archivo)

        elif opcion == "7":
            archivo = input("Nombre del archivo para cargar (con .json): ")
            inventario.cargar_desde_archivo(archivo)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
