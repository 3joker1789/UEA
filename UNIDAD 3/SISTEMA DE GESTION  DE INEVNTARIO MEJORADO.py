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
    def __init__(self, archivo_inventario='inventario.txt'):
        self.archivo_inventario = archivo_inventario
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = {}
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                for linea in archivo:
                    codigo, nombre, cantidad = linea.strip().split(',')
                    productos[codigo] = {'nombre': nombre, 'cantidad': int(cantidad)}
        except FileNotFoundError:
            print(f"Archivo {self.archivo_inventario} no encontrado. Se creará uno nuevo.")
        except PermissionError:
            print(f"No se tienen permisos para leer el archivo {self.archivo_inventario}.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for codigo, datos in self.productos.items():
                    archivo.write(f"{codigo},{datos['nombre']},{datos['cantidad']}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"No se tienen permisos para escribir en el archivo {self.archivo_inventario}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, codigo, nombre, cantidad):
        self.productos[codigo] = {'nombre': nombre, 'cantidad': cantidad}
        self.guardar_inventario()

    def actualizar_producto(self, codigo, cantidad):
        if codigo in self.productos:
            self.productos[codigo]['cantidad'] = cantidad
            self.guardar_inventario()
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
        else:
            print("Producto no encontrado.")
