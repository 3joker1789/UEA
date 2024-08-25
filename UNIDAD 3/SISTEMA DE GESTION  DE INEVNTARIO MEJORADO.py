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

import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos del archivo al iniciar el programa."""
        if not os.path.exists(self.archivo):
            self.crear_archivo()
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[id_producto] = {
                        'nombre': nombre,
                        'cantidad': int(cantidad),
                        'precio': float(precio)
                    }
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for id_producto, datos in self.productos.items():
                    file.write(f"{id_producto},{datos['nombre']},{datos['cantidad']},{datos['precio']}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def crear_archivo(self):
        """Crea un archivo vacío si no existe."""
        try:
            with open(self.archivo, 'w') as file:
                pass
        except PermissionError:
            print("Error: Permiso denegado para crear el archivo.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario y guarda los cambios en el archivo."""
        if id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[id_producto] = {
                'nombre': nombre,
                'cantidad': cantidad,
                'precio': precio
            }
            self.guardar_inventario()

    def actualizar_producto(self, id_producto, cantidad, precio):
        """Actualiza la cantidad y el precio de un producto existente y guarda los cambios en el archivo."""
        if id_producto in self.productos:
            self.productos[id_producto]['cantidad'] = cantidad
            self.productos[id_producto]['precio'] = precio
            self.guardar_inventario()
        else:
            print("El producto no existe en el inventario.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario y guarda los cambios en el archivo."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
        else:
            print("El producto no existe en el inventario.")

# Ejemplo de uso:
inventario = Inventario()

# Añadir un producto
inventario.añadir_producto('001', 'Laptop', 10, 999.99)

# Actualizar un producto
inventario.actualizar_producto('001', 8, 949.99)

# Eliminar un producto
inventario.eliminar_producto('001')

