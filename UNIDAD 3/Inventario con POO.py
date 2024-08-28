import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    # ... (otros métodos)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.productos = json.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado.")

# Ejemplo de uso:
inventario = Inventario()
inventario.cargar_inventario("inventario.json")

while True:
    print("1. Agregar producto")
    # ... (otras opciones del menú)
    opcion = input("Ingrese una opción: ")
    # ... (lógica del menú)