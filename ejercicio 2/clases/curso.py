from clases.alumno import Alumno

# Clase Curso, con su nombre y una lista de alumnos
class Curso:
    # Constructor de la clase
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.alumnos = []
    
    # Método para listar los alumnos 
    def listar_alumnos(self):
        print(f"\n-- CURSO {self.nombre_curso} --")
        # Se verifica que hay almunos en el curso
        if self.alumnos != []:
            for a in self.alumnos:
                print(a.mostrar_alumno())
        else:
            print ("\nNo hay alumnos inscritos.")

    # Método para inscribir un alumno al curso
    def inscribir(self, alumno:Alumno):
        self.alumnos.append(alumno)
        print(f"\nAlumno '{alumno.nombre_alumno}' inscrito en el curso {self.nombre_curso}.")

        # Consultar por consola si quiere ver el estado del curso
        aux = input("Desea consultar el estado del curso?(Si - No): ")
        if aux.lower() == "si":
            self.listar_alumnos()

    # Método para remover un alumno del curso
    def remover(self, alumno):
        aux = 0
        for a in self.alumnos:
            if alumno.lower() == a.nombre_alumno.lower():
                self.alumnos.remove(a)
                print(f"\nAlumno '{alumno}' removido.")
                aux += 1
            
        if aux == 0:
            print(f"\nNo está inscrito el alumno {alumno}.")
        
        # Consultar por consola si quiere ver el estado del curso
        aux = input("Desea consultar el estado del curso?(Si - No): ")
        if aux.lower() == "si":
            self.listar_alumnos()