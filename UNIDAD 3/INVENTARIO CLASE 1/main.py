#Clase Producto: Debe contener atributos como ID (único), nombre, cantidad y precio. Implementa métodos para obtener y establecer estos atributos.

#Clase Inventario: Debe utilizar una colección adecuada (p. ej., un diccionario) para almacenar los productos. Implementa métodos para:
print('IMPORTADORA ASTUDILLO S.A.')
AÑO= int(input("AÑO: "))

MES= int(input("MES: "))

DIA= int(input("DIA: "))
from inventario import Producto, Inventario

def menu():
    print("\nSistema de Gestión de Inventario")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

def main():
    inventario = Inventario()
    archivo = 'inventario.json'

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio = input("Nuevo precio (deja vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None, precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            for producto in resultados:
                print(producto)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            inventario.guardar_en_archivo(archivo)

        elif opcion == '7':
            inventario.cargar_desde_archivo(archivo)

        elif opcion == '8':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
