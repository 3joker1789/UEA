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
root.geometry("400x400")

# Aplicando colores personalizados a la ventana principal y widgets
root.config(bg="#000000")  #ROJO

# Treeview para mostrar los eventos
columns = ('Fecha', 'Hora', 'Descripción')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10)

# Cambiando el estilo del Treeview
style = ttk.Style()
style.configure("Treeview", background="#FFFFFF", foreground="#FF0000", fieldbackground="#D3D3D3")
style.configure("Treeview.Heading", background="#0000FF", foreground="#0000FF", font=("Helvetica", 10, "bold"))

# Entradas y etiquetas
frame_inputs = tk.Frame(root, bg="#D3D3D3")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Fecha", bg="#90EE90", fg="#000000").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_inputs)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Hora", bg="#90EE90", fg="#000000").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_inputs)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Descripción", bg="#90EE90", fg="#000000").grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_inputs)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# Botones
frame_buttons = tk.Frame(root, bg="#ADD8E6")
frame_buttons.pack(pady=10)

btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento, bg="#FF0000", fg="#FFFFFF", activebackground="#FF4500", activeforeground="#FFFFFF")  # Fondo Naranja
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="#FF0000", fg="#FFFFFF", activebackground="#A52A2A", activeforeground="#FFFFFF")  # Fondo Rojo y Marrón activo
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_buttons, text="Salir", command=root.quit, bg="#A9A9A9", fg="#FFFFFF", activebackground="#808080", activeforeground="#FFFFFF")  # Fondo Gris Oscuro
btn_salir.grid(row=0, column=2, padx=5)

root.mainloop()



