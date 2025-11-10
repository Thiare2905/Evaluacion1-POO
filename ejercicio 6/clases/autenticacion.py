from clases.usuario import Usuario

# Clase Autenticación
class Autenticacion:
    # Constructor de clase, con una lista de usuarios
    def __init__(self):
        self.usuarios = []

    # Método para registras un nuevo usuario que no exista
    def registrar_usuario(self, usuario:Usuario):
        if usuario in self.usuarios:
            return f"El usuario {usuario.nombre_usuario} ya existe."
        else:
            self.usuarios.append(usuario)
            return f"Se registro un nuevo usuario: {usuario.nombre_usuario}"
    
    # Método para iniciar sesión con usuario y contraseña
    def iniciar_sesion(self, usuario, contraseña):
        aux = 0
        for i in self.usuarios:
            if i.nombre_usuario == usuario:
                aux += 1
                if i.contraseña == contraseña:
                    return f"\nAcceso concedido. Bienvenido {i.nombre_usuario}."
        if aux == 1:
            return f"\nAcceso denegado. Contraseña invalida."
        else:
            return f"\nAcceso denegado. Usuario no encontrado."
    
    # Método para ver si un usuario está registrado
    def buscar_usuario(self, usuario):
        for u in self.usuarios:
            if u.nombre_usuario == usuario:
                return f"\nEl usuario '{u.nombre_usuario}' si está registrado."
        return f"\nEl usuario '{usuario}' no está registado."