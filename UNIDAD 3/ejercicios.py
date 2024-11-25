def greet(name, last_name):
    print("Hola",name, last_name)
greet("Ramiro","Saritama")
greet("Verito",  "Astudillo")


def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Seleccioe una operacion")
        print("1.Suma")
        print("2.Resta")
        print("3. Multipicacion")
        print("4 Division")
        print("5.Salir")

        option=int(input("Ingrese su opcion (1,2,3,4,5):"))
        if option==5:
            print("Saliendo de la calculadora")
            break

        if option in ["1","2","3","4"]:
            num1= float(input("ingrese primer numero:"))
            num2= float(input("ingrese el segundo numero:"))

            if option=="1":
                print("la suma es:",add(num1, num2))
            elif option=="2":
                print("La resta es :", substract(num1,num2))
            elif option=="3":
                print("La Multiplicacion es:", multiply(num1,num2))
            elif option=="4":
                print("La division es:", divide(num1,num2))

        else:
            print("Opcion no valida, porfavor intenta de nuevo ")

calculator()








