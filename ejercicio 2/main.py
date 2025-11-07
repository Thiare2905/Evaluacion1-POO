from clases.curso import Curso
from clases.alumno import Alumno

# Se instancian alumnos de clase Alumnos
alumno1 = Alumno("Pedro")
alumno2 = Alumno("Camila")
alumno3 = Alumno("Roberto")

# Se instancia un curso de clase Curso
curso = Curso("POO")

# Se usa el método para inscribir los alumnos al curso
curso.inscribir(alumno1)
curso.inscribir(alumno2)
curso.inscribir(alumno3)

# Se usa método para remover un alumno
curso.remover("Camila")
