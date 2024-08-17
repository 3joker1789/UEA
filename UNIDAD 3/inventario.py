#NUESTRO CLIENTE  NOS PIDE QUE LE REALIZEMOS UN INVENTARIO DE SUS
REPUESTOS DE REFRIGERACION YA QUE SU EMPRESA ESTA EN CRECIMIENTO Y DEBE DE MEJORAR SU REGISTRO

print('SERVIFRIO')

AÑO= int(input("AÑO: "))

MES= int(input("MES: "))

#CLASE PRODUCTO
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
#CLASE INVENTARIO
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(prod.get_id() == producto.get_id() for prod in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [prod for prod in self.productos if prod.get_id() != id_producto]
        print("Producto eliminado exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for prod in self.productos:
                print(prod)
#MENU DE PRODUCTOS
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        item = input("Selecciona una item: ")

        if item == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif item == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif item == '3':
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif item == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif item == '5':
            inventario.mostrar_todos_los_productos()

        elif item == '6':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
