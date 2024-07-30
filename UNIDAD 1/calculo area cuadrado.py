# CALCULAR VOLUMEN  DE CUARTO FRIO  #
print("UNIVERSIDAD ESTATAL AMAZONICA")
str(input('Nombre Alumno:'))
a = float(input('Ancho:'))
b = float(input('Largo:'))
c = float(input('Altura:'))

# Multiplicacion de sus lados para sacar un volumen del cuerpo #
volumen = a * b * c

print(f'Volumen: {volumen} m³')
# Evaluamos si resultado se manteniene en positivo caso contrario no es valido#

if volumen >= 0:
    print('Es valido.')
elif Resultado_total <= 0:
    print('Es indeterminado.')

# Calulo del area total de las paredes
# Dos paredes de ancho y largo
area_ancho_largo = (a * b)
area_total = area_ancho_largo
print(f'Area total de las paredes: {area_total}m²')
