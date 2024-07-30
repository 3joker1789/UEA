# Clase Padre (Superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


# Clase Hija (Subclase) Perro
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice Guau!"


# Clase Hija (Subclase) Gato
class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau!"


# Clase Hija (Subclase) Pájaro
class Pajaro(Animal):
    def hablar(self):
        return f"{self.nombre} dice Pío!"


# Función que demuestra el polimorfismo
def hacer_hablar_animales(animales):
    for animal in animales:
        print(animal.hablar())


# Función principal para ejecutar el programa
def main():
    # Crear instancias de las clases hijas
    animales = [
        Perro("Firulais"),
        Gato("Whiskers"),
        Pajaro("Tweety")
    ]

    # Llamar a la función que demuestra el polimorfismo
    hacer_hablar_animales(animales)


# Ejecutar la función principal
if __name__ == "__main__":
    main()
