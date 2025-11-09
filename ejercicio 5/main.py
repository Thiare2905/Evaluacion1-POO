from clases.pelicula import Pelicula
from clases.catalogo import Catalogo

# Se instancia el catalogo de clase Catalogo
catalogo = Catalogo()

# Se instancian las peliculas de clase Pelicula
pelicula1 = Pelicula("Moana: Un mar de aventuras", "Animación", 2016)
pelicula2 = Pelicula("Jurassic World: Dominio", "Accion", 2022)
pelicula3 = Pelicula("Orgullo y prejuicio", "Romance", 2005)
pelicula4 = Pelicula("Maze Runner: Correr o morir", "Accion", 2014)
pelicula5 = Pelicula("Yo antes de ti", "Romance", 2016)

# Se registran las peliculas en el catalogo
catalogo.registrar_peli(pelicula1)
catalogo.registrar_peli(pelicula2)
catalogo.registrar_peli(pelicula3)
catalogo.registrar_peli(pelicula4)
catalogo.registrar_peli(pelicula5)

# Se busca una pelicula por titulo
print(catalogo.buscar_titulo("Moana: Un mar de aventuras"))
# Se pregunta si quiere ver el catalogo
catalogo.preg_ver()
# Se buscan peliculas por genero
catalogo.buscar_genero("Romance")
# Se pregunta si quiere ver el catalogo
catalogo.preg_ver()