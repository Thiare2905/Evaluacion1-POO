from clases.medicion import Medicion
from clases.sensor import Sensor

# Se instancian mediciones clase Medición con sus valores
medicion1 = Medicion(2)
medicion2 = Medicion(3)
medicion3 = Medicion(5)
medicion4 = Medicion(6)

# Se instancia el sensor clase Sensor
sensor = Sensor("Sensor2000")

# Se registran las mediciones en el sensor
sensor.registrar_medicion(medicion1)
sensor.registrar_medicion(medicion2)
sensor.registrar_medicion(medicion3)
sensor.registrar_medicion(medicion4)

# Se muestra el valor máximo, mínimo y el promedio de las mediciones
print(f"\nValor máximo: {sensor.max_valor()}")
print(f"Valor mínimo: {sensor.min_valor()}")
print(f"Promedio: {sensor.promedio()}\n")

# Se muestra un resumen del sensor con todos sus datos
sensor.ver_resumen()