
import threading
# Definimos una variable global compartida
contador_global = 5
# Creamos un objeto mutex
mutex = threading.Lock()
# Función que incrementa el contador global de forma segura utilizando un mutex
def incrementar():
 global contador_global
# Adquirimos el mutex
mutex.acquire()
try:
# Sección crítica: Incrementamos el contador
  contador_global += 1
finally:
# Liberamos el mutex
  mutex.release()
# Función que ejecuta la tarea de incrementar el contador un número determinado de veces
def tarea():
 for _ in range(100000):
   incrementar()
# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
# Iniciamos los hilos
hilo1.start()
hilo2.start()
# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()
# Imprimimos el valor final del contador global
print("El valor final del contador global es:", contador_global)
import threading
# Creamos una barrera para sincronizar dos hilos
barrera = threading.Barrier(2)
# Función que ejecuta la tarea de imprimir un mensaje y esperar en la barrera
def tarea():
 print("Hilo iniciado")
# Esperamos en la barrera
 barrera.wait()
 print("Hilo continuando")
# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
# Iniciamos los hilos
hilo1.start()
hilo2.start()
# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()
print("Programa terminado")
import threading
import time
# Creamos un objeto evento
evento = threading.Event()
# Función que espera a que se active el evento
def esperar_evento():
 print("Esperando al evento...")
# Esperamos a que el evento se active
evento.wait()
print("El evento ha sido activado!")
# Función que activa el evento después de un cierto tiempo
def activar_evento():
 print("Esperando 5 segundos antes de activar el evento...")
time.sleep(5)
# Activamos el evento
evento.set()
print("El evento ha sido activado después de 5 segundos")
# Creamos dos hilos que ejecutarán las funciones
hilo1 = threading.Thread(target=esperar_evento)
hilo2 = threading.Thread(target=activar_evento)
# Iniciamos los hilos
hilo1.start()
hilo2.start()
# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()
print("Programa terminado")