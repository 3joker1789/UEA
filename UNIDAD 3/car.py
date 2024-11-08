import customtkinter as ctk
from tkinter import messagebox

# Sample data
cars = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "Honda": ["Accord", "Civic", "CR-V"],
    "Ford": ["Focus", "Fusion", "Mustang"]
}

# Initialize the main application window
app = ctk.CTk()
app.title("Car Chooser")
app.geometry("400x400")

# Function to display selected car details
def show_selection():
    make = make_var.get()
    model = model_var.get()
    year = year_var.get()
    color = color_var.get()
    message = f"Selected Car:\nMake: {make}\nModel: {model}\nYear: {year}\nColor: {color}"
    messagebox.showinfo("Car Selection", message)

# Variables to store user selections
make_var = ctk.StringVar()
model_var = ctk.StringVar()
year_var = ctk.StringVar()
color_var = ctk.StringVar()

# Dropdown for car make
make_label = ctk.CTkLabel(app, text="Select Make:")
make_label.pack(pady=10)
make_dropdown = ctk.CTkOptionMenu(app, variable=make_var, values=list(cars.keys()))
make_dropdown.pack(pady=10)

# Dropdown for car model, updated based on selected make
def update_model_dropdown(*args):
    selected_make = make_var.get()
    models = cars.get(selected_make, [])
    model_var.set("")
    model_dropdown.configure(values=models)

make_var.trace("w", update_model_dropdown)
model_label = ctk.CTkLabel(app, text="Select Model:")
model_label.pack(pady=10)
model_dropdown = ctk.CTkOptionMenu(app, variable=model_var, values=[])
model_dropdown.pack(pady=10)

# Dropdown for car year
year_label = ctk.CTkLabel(app, text="Select Year:")
year_label.pack(pady=10)
year_dropdown = ctk.CTkOptionMenu(app, variable=year_var, values=[str(year) for year in range(2000, 2025)])
year_dropdown.pack(pady=10)

# Dropdown for car color
color_label = ctk.CTkLabel(app, text="Select Color:")
color_label.pack(pady=10)
color_dropdown = ctk.CTkOptionMenu(app, variable=color_var, values=["Red", "Blue", "Black", "White", "Silver"])
color_dropdown.pack(pady=10)

# Button to confirm selection
confirm_button = ctk.CTkButton(app, text="Show Selection", command=show_selection)
confirm_button.pack(pady=20)

# Run the application
app.mainloop()