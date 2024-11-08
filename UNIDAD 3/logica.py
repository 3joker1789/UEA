#Edad de usuario
#Pedimos edad de Usuario
edad = int(input("Ingresa la edad por favor:"))
permiso_padres = input("Tiene permiso de sus padres:")
#evaluamos segun la condicionales
if edad ≥ 18:
    print("Ingreso Permitido")
elif edad > 16 and edad < 18 and permiso_padres.casefold() ="si":
    print("ingreso Permitido.")
else:
    print("ingreso denegado")