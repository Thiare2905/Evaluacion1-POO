from clases.libro import Libro
from clases.biblioteca import Biblioteca

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1)
libro2 = Libro("El Señor de los Anillos", "J. R. R. Tolkien", 7)

biblioteca = Biblioteca("La mejor biblioteca")

biblioteca.registrar(libro1)
biblioteca.registrar(libro2)

biblioteca.mostrar_catalogo()
print(biblioteca.buscar_libro("El Principito"))
print(biblioteca.prestamo("El Señor de los Anillos"))
print(biblioteca.devolucion("El Señor de los Anillos"))