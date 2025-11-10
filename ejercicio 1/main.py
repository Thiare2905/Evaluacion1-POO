from clases.libro import Libro
from clases.biblioteca import Biblioteca

# Se crean libros de clase Libo
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1)
libro2 = Libro("El Señor de los Anillos", "J. R. R. Tolkien", 7)

# Se crea una biblioteca de clase Biblioteca
biblioteca = Biblioteca("La mejor biblioteca")

# Se registan los libros en la biblioteca
biblioteca.registrar(libro1)
biblioteca.registrar(libro2)

# Se muestra el catalogo
biblioteca.mostrar_catalogo()
# Se busca un libro por su titulo
print(biblioteca.buscar_libro("El Principito"))
# Se registra un prestamo
print(biblioteca.prestamo("El Señor de los Anillos"))
# Se registra una devolución
print(biblioteca.devolucion("El Señor de los Anillos"))