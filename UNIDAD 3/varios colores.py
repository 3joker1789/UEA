dark_colors = [
    "#2B2B2B",  # Gris oscuro
    "#1C1C1C",  # Negro casi puro
    "#0D47A1",  # Azul oscuro intenso
    "#283593",  # Azul medianoche
    "#4A148C",  # Púrpura oscuro
    "#1B5E20",  # Verde oscuro bosque
    "#212121",  # Gris carbón
    "#263238",  # Gris azulado oscuro
    "#4E342E",  # Marrón chocolate oscuro
    "#3E2723",  # Marrón profundo
    "#BF360C",  # Rojo oscuro quemado
    "#3E1F47",  # Púrpura berenjena
    "#0D3B66",  # Azul marino profundo
    "#1A237E",  # Azul real oscuro
    "#311B92",  # Púrpura imperial oscuro
    "#004D40",  # Verde pino oscuro
    "#2C3E50",  # Azul grisáceo oscuro
    "#424242",  # Gris oscuro mediano
    "#37474F",  # Gris plomo
    "#5D4037",  # Marrón oscuro caoba
]

# Ejemplo de uso con tkinter
import tkinter as tk

root = tk.Tk()

for idx, color in enumerate(dark_colors):
    label = tk.Label(root, text=f"Dark Color {idx+1}", bg=color, fg="white")
    label.pack(fill=tk.X)

root.mainloop()
