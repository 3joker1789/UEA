import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'Producto[ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}]'


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id_producto] = producto
        print(f"Producto {producto.nombre} añadido al inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [prod for prod in self.productos.values() if prod.nombre == nombre]
        return resultados

    def mostrar_todos_los_productos(self):
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
