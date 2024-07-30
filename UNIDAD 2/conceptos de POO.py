# UNIVERSIAD ESTATAL AMAZONICA#
class Mantenimiento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tarea(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


# Clase Hija (Subclase) Ramiro
class Senior(Tecnico):
    def tarea(self):
        return f"{self.nombre} Electrico!"


# Clase Hija (Subclase) Andres
class Junior(Tecnico):
    def tarea(self):
        return f"{self.nombre} Ayudante!"


# Clase Hija (Subclase) Pájaro
class Novato(Tecnico):
    def tarea(self):
        return f"{self.nombre} Aprendiz!"


# Función que demuestra el polimorfismo
def dar_tarea_Tecnicos(Tecnicos):
    for tecnico in Tecnicos:
        print(tecnico.tarea())


# Función principal para ejecutar el programa
def main():
    # Crear instancias de las clases hijas
    Tecnicos = [
        Senior("Ramiro"),
        Junior("Andres"),
        Novato("Zuniga")
    ]

    # Llamar a la función que demuestra el polimorfismo
    dar_tareas_Tecnicos(Tecnicos)


# Ejecutar la función principal
if __name__ == "__main__":
    main()
