# Clase Libro
class Libro:
    # Constructor de clase, inizializada por titulo, autor y numero de copias
    def __init__(self, titulo, autor, numero_copias):
        self.titulo = titulo
        self.autor = autor
        self.numero_copias = numero_copias

    # Método para mostrar un libro
    def mostrar_libro(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Copias disponibles: {self.numero_copias}"