from clases.item import Item
from clases.pedido import Pedido

# Se instancian los items de clase Item
item1 = Item("Hamburguesa", 7900, 4)
item2 = Item("Papas fritas", 2500, 7)
item3 = Item("Helado", 1900, 2)

# Se instancia el pedido de clase Pedido
pedido = Pedido(1)

# Se registran los items en el pedido
pedido.registrar_item(item1)
pedido.registrar_item(item2)
pedido.registrar_item(item3)

# Se muestra el total del pedido
print(pedido.calcular_total())