class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.autor_titulo = (autor, titulo)

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"
