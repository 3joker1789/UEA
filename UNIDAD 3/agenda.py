import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()
    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, llena todos los campos")

def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento?")
        if respuesta:
            tree.delete(selected_item)

def limpiar_campos():
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

root = tk.Tk()
root.title("Agenda Personal")

# Treeview para mostrar los eventos
columns = ('Fecha', 'Hora', 'Descripción')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10)

# Entradas y etiquetas
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_inputs)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Hora").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_inputs)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_inputs)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_agregar
