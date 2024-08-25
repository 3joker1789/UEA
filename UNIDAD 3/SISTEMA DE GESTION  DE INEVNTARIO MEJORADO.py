#Tarea: Sistema de Gestión de Inventarios Mejorado

#Objetivo: Mejorar el sistema de gestión de inventarios desarrollado anteriormente para que utilice archivos para almacenar y recuperar la información del inventario y maneje excepciones durante la lectura y escritura de archivos.

#Nuevos Requisitos:

    #Almacenamiento de Inventarios en Archivos:
        #Modificar la clase Inventario para que al añadir,actualizar, o eliminar productos, estas modificaciones se reflejen en un archivo de texto (por ejemplo, inventario.txt).

    #Recuperación de Inventarios desde Archivos:
        #Al iniciar el programa, cargar automáticamente los productos existentes en inventario.txt para reconstruir el inventario.

    #Manejo de Excepciones:
        #Implementar manejo de excepciones para capturar y tratar adecuadamente posibles errores durante la manipulación de archivos, como FileNotFoundError y PermissionError.
        #Asegurar que el programa maneje casos en los que el archivo de inventario no exista, creándolo si es necesario.

    #Modificaciones a la Interfaz de Usuario en la Consola:
        #Actualizar la interfaz de usuario para notificar al usuario sobre el éxito o fallo de operaciones de archivo (por ejemplo, notificar al usuario cuando un producto se añade exitosamente al archivo de inventario).

#Instrucciones Adicionales:

    #Mantén la organización y claridad del código, asegurando que todas las modificaciones estén bien comentadas para explicar el funcionamiento del manejo de archivos y excepciones.
    #Realiza pruebas exhaustivas para asegurarte de que el programa puede manejar situaciones como archivos corruptos, falta de permisos de escritura, y más.

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            self.crear_archivo()
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    datos = linea.strip().split(',')
                    id_producto = datos[0]
                    self.productos[id_producto] = {
                        'nombre': datos[1],
                        'categoria': datos[2],
                        'cantidad': int(datos[3]),
                        'precio': float(datos[4]),
                        'proveedor': datos[5],
                        'fecha_ingreso': datos[6],
                        'ubicacion': datos[7],
                        'notas': datos[8]
                    }
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for id_producto, datos in self.productos.items():
                    file.write(f"{id_producto},{datos['nombre']},{datos['categoria']},"
                               f"{datos['cantidad']},{datos['precio']},{datos['proveedor']},"
                               f"{datos['fecha_ingreso']},{datos['ubicacion']},{datos['notas']}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, id_producto, nombre, categoria, cantidad, precio, proveedor, fecha_ingreso, ubicacion, notas):
        if id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[id_producto] = {
                'nombre': nombre,
                'categoria': categoria,
                'cantidad': cantidad,
                'precio': precio,
                'proveedor': proveedor,
                'fecha_ingreso': fecha_ingreso,
                'ubicacion': ubicacion,
                'notas': notas
            }
            self.guardar_inventario()

    # Métodos para actualizar y eliminar productos serían similares, con la estructura de datos ampliada.

# Ejemplo de uso:
inventario = Inventario()

# Añadir un producto
inventario.añadir_producto('001', 'Compresor LG QK-134', 'Compresores', 15, 150.00, 'LG Electronics', '2024-08-20', 'Estante A1', 'Modelo QK-134')

