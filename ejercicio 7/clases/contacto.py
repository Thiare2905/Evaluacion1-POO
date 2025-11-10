# Clase Contacto
class Contacto:
    # Contructor de clase, inicializada con nombre, numero de telefono y correo
    def __init__(self, nombre, num_telefono, correo):
        self.nombre = nombre
        self.num_telefono = num_telefono
        self.correo = correo

    # Método para ver un contacto
    def ver_contacto(self):
        return f"Nombre: {self.nombre} - Numero celular: {self.num_telefono} - Correo electrónico: {self.correo}"