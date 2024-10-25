##### SISTEMA DE HOSPITAL ####
from cmd import IDENTCHARS


def agregar_paciente(pacientes):
    nombre = input("Ingrese nombre del Paciente")
    if pacientes:
        id_paciente = max(pacientes.keys())+1
    else:
        id_paciente = 1
    pacientes[id_paciente] = nombre
    return f"\nPaciente (nombre) agregado con ID (id_paciente)\n"

def borrar_paciente(pacientes):
    id_paciente = int(input("Ingrese el ID del paciente a eliminar:"))
    if id_paciente in pacientes:
        nombre = pacientes[id_paciente]
        return f"\nSe elimino al paciente (nombre) con ID (id_paciente\n"
    else:
        return f"\nNo se encontro el ID (id_paciente) en la base de datos\n "

def buscar_paciente_por_id(pacientes):
    id_paciente = int(input("Ingresa el ID del paciente:"))
    if id_paciente in pacientes:
        nombre = pacientes[id_paciente]
        return  f"\n El usuario  con ID (Id_paciente) es (nombre)\n"
    else:
        return f"\nNo se encontro el paciente con el ID proporcionado\n"
def buscar_paciente_por_nombre(pacientes):
    nombre_buscar = input("Ingresa el nombre del paciente ")
    for id_paciente, nombre in pacientes.items():
        if nombre == nombre_buscar:
            return f"\nEl paciente con (nombre_buscar) tiene ID(id_paciente)\n"
        return f"\nNo se encontro un paciente con el nombre (nombre_buscar)\n"
def imprimir_todos_los_pacientes(pacientes):
    if not pacientes:
        return  "\nNo hay pacientes registrados.\n"
    lista_pacientes="\nLista de pacientes:\n"
    for id_paciente, nombre in pacientes.items():
        lista_pacientes +- f"ID: (id_paciente),Nombre:(nombre)\n"
        return lista_pacientes
pacientes ={}
salir = False

while not salir:
    print("""\nBienvenido al sistema de pacientes
    1.Agregar pacientes
    2.Borrar pacientes
    3.Buscar paciente por ID
    4.Buscar paciente por nombre
    5.Imprimir todos los pacientes
    6. Cerrar sistema""")

    opcion = input("Que deseas hacer? :")

    match opcion:
        case "1":
            print(agregar_paciente(pacientes))
        case "2":
            print(borrar_paciente(pacientes))
        case "3":
            print(buscar_paciente_por_id(pacientes))
        case "4":
            print(buscar_paciente_por_nombre(pacientes))
        case "5":
            print(imprimir_todos_los_pacientes(pacientes))
        case "6":
            print("\nCerrando sistema....")
            salir = True
        case _:
            print("Opcion no reconocida. Intenta de nuevo.")


_








