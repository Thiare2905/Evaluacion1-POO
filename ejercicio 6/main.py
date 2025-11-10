from clases.autenticacion import Autenticacion
from clases.usuario import Usuario

# Se crea una variable de clase Autenticacion
autenticacion = Autenticacion()

# Se crean usuarios de clase Usuario, con usuario y contraseña
usuario1 = Usuario("Jorge Muñoz", "123456")
usuario2 = Usuario("Matias Perez", "654321")
usuario3 = Usuario("Cecilia Gallardo", "123123")
usuario4 = Usuario("Alejandra Hernandez", "111111")

# Se registran los usuarios nuevos 
print(autenticacion.registrar_usuario(usuario1))
print(autenticacion.registrar_usuario(usuario2))
print(autenticacion.registrar_usuario(usuario3))
print(autenticacion.registrar_usuario(usuario4))

# Se inicia sesión con usuario y contraseña
print(autenticacion.iniciar_sesion("Matias Perez", "654321"))

# Se ve si está registrado un usuario
print(autenticacion.buscar_usuario("Cecilia gallardo"))