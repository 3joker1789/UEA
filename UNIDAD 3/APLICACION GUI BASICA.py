import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un dato válido")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("GUI")
ventana.geometry("450x350")

# Colores personalizados
ventana.config(bg="#000000")  # Fondo de la ventana

# Crear etiquetas y campos de texto
label = tk.Label(ventana, text="Ingresa un dato:", bg="#FF0000", fg="#333333", font=("Arial", 12))
label.pack(pady=10)

entrada = tk.Entry(ventana, width=40, bg="#FFFFFF", fg="#333333", font=("Arial", 10))
entrada.pack(pady=10)

# Crear el botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="#A9A9A9", fg="#000000", font=("Arial", 10, "bold"))
boton_agregar.pack(pady=10)

# Crear la lista para mostrar los datos
lista = tk.Listbox(ventana, width=40, height=10, bg="#ffffff", fg="#333333", font=("Arial", 10))
lista.pack(pady=10)

# Crear el botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista, bg="#f44336", fg="#ffffff", font=("Arial", 10, "bold"))
boton_limpiar.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
