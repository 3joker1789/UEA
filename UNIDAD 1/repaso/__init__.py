print('UNIVERSIDAD ESTATAL AMAZONICA ')
print('LA UNIVERSIDAD MAS GRANDE DE LA AMAZONIA ')
print('PROGRAMACION ORIENTADA A OBJETOS ')
print('SEGUNDO SEMESTRE')
print('PARALELO "B" ')
int(input('Numero de deber :'))
str(input('Nombre Alumno:'))
str(input('Mes:'))
int(input('Año:'))
int(input('Control de Temperatura ambiente del clima de la  semana: '))


class Ciudad:
    def __init__(self, nombre, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        self.nombre = nombre
        self.temperaturas = {
            'lunes': lunes,
            'martes': martes,
            'miercoles': miercoles,
            'jueves': jueves,
            'viernes': viernes,
            'sabado': sabado,
            'domingo': domingo
        }

    def atributos(self):
        print(self.nombre, ":", sep="")
        for dia, temp in self.temperaturas.items():
            print(f"{dia}: {temp}")

    def promedio_temperatura(self):
        total = sum(self.temperaturas.values())
        promedio = total / len(self.temperaturas)
        return promedio


print("Temperatura en °C")
mi_ciudad = Ciudad(nombre="Quito", lunes=12, martes=14, miercoles=13, jueves=14, viernes=21, sabado=12, domingo=12)

mi_ciudad.atributos()
print(f"Promedio de temperatura: {mi_ciudad.promedio_temperatura():.2f} °C")
