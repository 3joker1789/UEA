print('UNIVERSIDAD ESTATAL AMAZONICA')
print('Ramiro Saritama')
print('Paralelo "B"')


class heroe:
    nombre = 'Default'
    fuerza = 0
    IQ = 0
    vida = 0
    recursos = 0

    def __init__(self, nombre, fuerza, IQ, vida, recursos):
        self.nombre = nombre
        self.fuerza = fuerza
        self.IQ = IQ
        self.vida = vida
        self.recursos = recursos

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("fuerza:", self.fuerza)
        print("IQ:", self.IQ)
        print("vida:", self.vida)
        print("recursos:", self.recursos)


mi_heroe = heroe("Batman", 100, 25, 100, 1000000)
mi_heroe.atributos()
