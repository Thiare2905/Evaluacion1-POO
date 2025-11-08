from clases.item import Item

# Clase Pedido
class Pedido:
    # Constructor de clase
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.items = []
        self.total = 0

    # Método para registrar un item al pedido
    def registrar_item(self, item:Item):
        self.items.append(item)
        print(f"Se agregó {item.nombre} al pedido {self.numero_pedido}.")

    # Método para calcular el total del pedido y mostrar detalles del pedido
    def calcular_total(self):
        if self.items == []:
            return "Total a pagar: 0"
        else:
            for i in self.items:
                self.total += i.calcular_subtotal()
            self.ver_listado()
            return f"Total a pagar: {self.total}"
    
    # Método para listar los items en el pedido
    def ver_listado(self):
        print(f"\n-- Listado del Pedido {self.numero_pedido} --")
        if self.items != []:
            for p in self.items:
                print(p.mostrar_item())
        else:
            print(f"No se han agregado items al pedido {self.numero_pedido}.")