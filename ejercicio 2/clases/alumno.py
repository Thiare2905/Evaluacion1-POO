# Clase Alumno, se registra con su nombre
class Alumno:
    def __init__(self, nombre_alumno):
        self.nombre_alumno = nombre_alumno

    # Método para mostrar un alumno
    def mostrar_alumno(self):
        return f"Nombre: {self.nombre_alumno}."