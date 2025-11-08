# Clase Item
class Item:
    # Constructor de clase
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Método para calcular el total de cada item
    def calcular_subtotal(self):
        return self.precio * self.cantidad
    
    #Método para mostrar el item con sus detalles
    def mostrar_item(self):
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Cantidad: {self.cantidad} | Subtotal: {self.calcular_subtotal()}"