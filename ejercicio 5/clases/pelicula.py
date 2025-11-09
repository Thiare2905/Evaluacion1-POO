# Clase Pelicula
class Pelicula:
    # Constructor de clase, se inicializa con titulo, genero y año
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

    # Método que muestra la pelicula con su información
    def info_pelicula(self):
        return f"Titulo: '{self.titulo}' - Género: {self.genero} - Año de lanzamiento: {self.año}"