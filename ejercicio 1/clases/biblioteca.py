from clases.libro import Libro

class Biblioteca:
    def __init__(self, nombre_biblioteca):
        self.nombre_biblioteca = nombre_biblioteca
        self.libros = []

    def registrar(self, libro:Libro):
        self.libros.append(libro)

    def mostrar_catalogo(self):
        print("\n- CÁTALOGO")
        for l in self.libros:
            print(l.mostrar_libro())

    def buscar_libro(self, titulo):
        for l in self.libros:
            if titulo == l.titulo:
                return f"\n- LIBRO ENCONTRADO.\n{l.mostrar_libro()}"

    def prestamo(self, titulo):
        for l in self.libros:
            if titulo == l.titulo:
                if l.numero_copias >= 1:
                    l.numero_copias -= 1
                    return f"\n- PRÉSTAMO REALIZADO.\n{l.mostrar_libro()}"
                else:
                    return f"\n- El libro '{l.titulo}' no tiene copias disponibles"
            else:
                return f"\n- El libro '{titulo}' no fue encontrado."
            
    def devolucion(self, titulo):
        for l in self.libros:
            if titulo == l.titulo:
                l.numero_copias += 1
                return f"\n- DEVOLUCIÓN REALIZADA.\n{l.mostrar_libro()}"
        return f"\n- La biblioteca '{self.nombre_biblioteca}' no registró el libro '{titulo}'."