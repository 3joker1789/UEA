import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Colores para mejorar la interfaz
        self.bg_color = "#000000"  # Color de fondo
        self.completed_color = "#00ff00"  # Color para tareas completadas
        self.pending_color = "#ffffff"  # Color para tareas pendientes

        # Frame principal
        self.frame = tk.Frame(self.root, bg=self.bg_color)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Entrada de nueva tarea
        self.task_var = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.task_var, font=("Arial", 12), width=30)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        # Botones
        self.add_btn = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="black", font=("Arial", 10))
        self.add_btn.grid(row=0, column=1, padx=10)

        self.complete_btn = tk.Button(self.frame, text="Completar Tarea", command=self.complete_task, bg="#2196f3", fg="white", font=("Arial", 10))
        self.complete_btn.grid(row=1, column=1, padx=10)

        self.delete_btn = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336", fg="white", font=("Arial", 10))
        self.delete_btn.grid(row=2, column=1, padx=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.frame, height=15, selectmode=tk.SINGLE, font=("Arial", 12), bg=self.pending_color)
        self.task_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

        # Configurar atajos de teclado
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

        # Expansión de la lista
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, task)
            self.task_listbox.itemconfig(index, bg=self.completed_color)
        except IndexError:
            messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para completar.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para eliminar.")

# Crear la aplicación
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
