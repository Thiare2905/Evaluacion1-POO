from clases.libro import Libro

# Clase Biblioteca
class Biblioteca:
    # Constructor de clase
    def __init__(self, nombre_biblioteca):
        self.nombre_biblioteca = nombre_biblioteca
        self.libros = []

    # Método para registrar un libro en la biblioteca
    def registrar(self, libro:Libro):
        self.libros.append(libro)

    # Método para mostrar el catalogo
    def mostrar_catalogo(self):
        print("\n- CÁTALOGO")
        for l in self.libros:
            print(l.mostrar_libro())

    # Método para buscar un libro 
    def buscar_libro(self, titulo):
        for l in self.libros:
            if titulo.lower() == l.titulo.lower():
                return f"\n- LIBRO ENCONTRADO.\n{l.mostrar_libro()}"

    # Método para registrar un prestamo
    def prestamo(self, titulo):
        for l in self.libros:
            if titulo.lower() == l.titulo.lower():
                if l.numero_copias >= 1:
                    l.numero_copias -= 1
                    return f"\n- PRÉSTAMO REALIZADO.\n{l.mostrar_libro()}"
                else:
                    return f"\n- El libro '{l.titulo}' no tiene copias disponibles"
            else:
                return f"\n- El libro '{titulo}' no fue encontrado."
            
    # Método que registra una devolución
    def devolucion(self, titulo):
        for l in self.libros:
            if titulo.lower() == l.titulo.lower():
                l.numero_copias += 1
                return f"\n- DEVOLUCIÓN REALIZADA.\n{l.mostrar_libro()}"
        return f"\n- La biblioteca '{self.nombre_biblioteca}' no registró el libro '{titulo}'."