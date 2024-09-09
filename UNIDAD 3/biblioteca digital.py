# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla inmutable para almacenar autor y título
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase que representa un usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para los libros actualmente prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"

# Clase que representa la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurar que los IDs de usuario sean únicos

    # Añadir un libro a la biblioteca
    def anadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[1]}' añadido con éxito.")

    # Eliminar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado con éxito.")

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    # Prestar un libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]  # El libro ya no está disponible en la biblioteca
            print(f"Libro '{libro.info[1]}' prestado a {usuario.nombre}.")
        else:
            print("No se pudo realizar el préstamo. Verifica el ID de usuario y el ISBN.")

    # Devolver un libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = usuario.devolver_libro(isbn)
            if libro:
                self.libros[libro.isbn] = libro  # El libro regresa a la biblioteca
                print(f"Libro '{libro.info[1]}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario no tiene prestado un libro con ISBN {isbn}.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, criterio):
        resultados = []
        for libro in self.libros.values():
            if criterio.lower() in libro.info[1].lower() or criterio.lower() in libro.info[0].lower() or criterio.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con el criterio '{criterio}'.")

    # Listar libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

# Prueba del sistema de biblioteca
if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "1234")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "5678")
    biblioteca.anadir_libro(libro1)
    biblioteca.anadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan", "u001")
    usuario2 = Usuario("Ana", "u002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar un libro
    biblioteca.prestar_libro("u001", "1234")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("u001")

    # Devolver un libro
    biblioteca.devolver_libro("u001", "1234")

    # Buscar libros
    biblioteca.buscar_libros("Cervantes")

