print('UNIVERSIDAD ESTATAL AMAZONICA')
print('Ramiro Saritama')
print('Paralelo "B"')
print('SEGUNDO SEMESTRE')


class villano:
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

        print(f'Villano {self.nombre} creado.')

    def __del__(self):
        print(f'Villano {self.nombre} derrotado por Batman.')


mi_villano = villano('Joker', 85, 180, 100, 1000000)
print('El nombre del villano es', mi_villano.nombre)
print('La fuerza  del jugador es', mi_villano.fuerza)
print('El IQ  del jugador es', mi_villano.IQ)
print('La vida del jugador es', mi_villano.vida)
print('Los recursos  del jugador es', mi_villano.recursos)
