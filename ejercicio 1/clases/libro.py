class Libro:
    def __init__(self, titulo, autor, numero_copias):
        self.titulo = titulo
        self.autor = autor
        self.numero_copias = numero_copias

    def mostrar_libro(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Copias disponibles: {self.numero_copias}"