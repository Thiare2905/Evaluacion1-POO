from clases.pelicula import Pelicula

# Clase Catalogo
class Catalogo:
    # Constructor de la clase
    def __init__(self):
        self.peliculas = []

    # Método para registar una pelicula en el catalogo
    def registrar_peli(self, pelicula:Pelicula):
        self.peliculas.append(pelicula)
        print(f"\nSe registro {pelicula.titulo} con éxito.")
        self.preg_ver()

    # Método que muestra el catalogo con sus peliculas
    def ver_catalogo(self):
        i = 1
        print("\n  -- Catálogo --")
        for p in self.peliculas:
            print(f"{i}. Película '{p.titulo}'\n   Género: {p.genero} - Año de lanzamiento: {p.año}")
            i += 1

    # Método para buscar una pelicula por su titulo
    def buscar_titulo(self, titulo):
        print("\n-- Busqueda por título")
        for p in self.peliculas:
            if p.titulo.lower() == titulo.lower():
                return f"La película '{titulo}' SI está en el catalogó.\n{p.info_pelicula()}\n"
        return f"No se encontró la pelicula '{titulo}'\n."
    
    # Método para buscar peliculas por genero
    def buscar_genero(self, genero):
        print("\n-- Busqueda por género")
        aux = 0
        for p in self.peliculas:
            if p.genero.lower() == genero.lower():
                print(p.info_pelicula())
            else:
                aux += 1
                if aux == len(self.peliculas):
                    print(f"No se encontraron peliculas con el género {genero}." )

    # Método para preguntar si quiere ver el catalogo
    def preg_ver(self):
        ver = input("Desea ver el catalogó? (Si - No): ")
        if ver.lower() == 'si':
            self.ver_catalogo()        