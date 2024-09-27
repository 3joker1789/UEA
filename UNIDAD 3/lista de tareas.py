import tkinter as tk
from tkinter import messagebox


class TaskListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.configure(bg="#000000")

        # Crear el campo de entrada con color de fondo y borde
        self.task_entry = tk.Entry(root, width=40, bg="#f0f8ff", bd=2)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Añadir tarea al presionar Enter

        # Botones con color de fondo
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="#", fg="black")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task, bg="#f0e68c",
                                         fg="black")
        self.complete_button.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="#ff7f7f", fg="black")
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Lista de tareas (Listbox) con fondo y color de texto
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg="#ffffe0", fg="black")
        self.task_listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)  # Doble clic para marcar como completada

    # Función para añadir tareas
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    # Función para marcar una tarea como completada
    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            completed_task = f"✔ {task}"
            self.task_listbox.delete(selected_task_index)
            # Añadir tarea completada con un color diferente (verde)
            self.task_listbox.insert(selected_task_index, completed_task)
            self.task_listbox.itemconfig(selected_task_index, {'fg': 'green'})  # Cambiar el color de texto a verde
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    # Función para eliminar una tarea
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")


# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskListApp(root)
    root.mainloop()
