from clases.agenda import Agenda
from clases.contacto import Contacto

# Se crea una agenda clase Agenda
agenda = Agenda()

# Se crean contactos de clase Contacto
contacto1 = Contacto("Johan", 972343845, "johan@gmail.cl")
contacto2 = Contacto("Maria", 972111145, "maria@gmail.cl")
contacto3 = Contacto("Pablo", 992243800, "pablo@gmail.cl")

# Se añaden los contactos a la agenda y se pergunta si la quiere ver
print(agenda.agregrar_contacto(contacto1))
agenda.lista_contactos()
print(agenda.agregrar_contacto(contacto2))
agenda.lista_contactos()
print(agenda.agregrar_contacto(contacto3))
agenda.lista_contactos()

# Se busca un contacto por el nombre
print(agenda.buscar_contacto("Johan"))
agenda.lista_contactos()

# Se elimina un contacto por cualquier dato
print(agenda.eliminar_contacto("pablo@gmail.cl"))
agenda.lista_contactos()