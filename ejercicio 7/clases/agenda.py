from clases.contacto import Contacto
# Clase Agenda
class Agenda:
    # Constructor de clase 
    def __init__(self):
        self.contactos = []

    # Método para agregar un contacto a la agenda
    def agregrar_contacto(self, contacto:Contacto):
        self.contactos.append(contacto)
        return f"\nSe agregó el contacto '{contacto.nombre}'."

    # Método para mostrar la agenda
    def lista_contactos(self):
        preg = input("¿Quiere ver la agenda? (Si-No): ")
        if preg.lower() == "si":
            print(" -- Agenda --")
            for c in self.contactos:
                print(c.ver_contacto())

    # Método para buscar un contacto
    def buscar_contacto(self, contacto):
        for c in self.contactos:
            if contacto.lower() == c.nombre.lower():
                return f"\nSe encontró el contacto: '{contacto}'\n{c.ver_contacto()}"
        return f"\nNo se encontró el contacto '{contacto}'."
    
    # Método para eliminar un contacto
    def eliminar_contacto(self, dato):
        for c in self.contactos:
            if dato == c.nombre or dato == c.num_telefono or dato == c.correo:
                self.contactos.remove(c)
                return f"\nSe eliminó el contacto '{c.nombre}'."
        return "\nNo se encontró en agenda para eliminar."