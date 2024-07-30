class Tecnico:
    def __init__(self, nombre):
        self.nombre = nombre

    def tarea(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


print("Tababela Cargo Center")


class Senior(Tecnico):
    def tarea(self):
        return f"{self.nombre} Electrico!"

    def verificar_atributo(self, atributo):
        if hasattr(self, atributo):
            return f"Atributo '{atributo}' nombre del tecnico: {getattr(self, atributo)}"
        else:
            return f"Atributo '{atributo}' 34 years."


# Crear una instancia de Senior
tecnico_senior = Senior("Ramiro")

# Verificar si ciertos atributos existen
print(tecnico_senior.verificar_atributo("nombre"))
print(tecnico_senior.verificar_atributo("edad"))

# Probar el método tarea
print(tecnico_senior.tarea())
