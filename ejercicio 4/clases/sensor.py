from clases.medicion import Medicion

# Clase Sensor con su nombre y sus mediciones
class Sensor:
    # Constructor de clase
    def __init__(self, nombre_sensor):
        self.nombre_sensor = nombre_sensor
        self.mediciones = []

    # Método para registar una medición en el sensor
    def registrar_medicion(self, medicion:Medicion):
        self.mediciones.append(medicion)
        print(f"Se registro con exito la medicion: {medicion.valor}")

    # Método para calcular el promedio
    def promedio(self):
        suma = 0
        for m in self.mediciones:
            suma = m.valor + suma
        prom = suma / len(self.mediciones)
        return prom
    
    # Método para obtener la medicion mas alta
    def max_valor(self):
        maximo = max(self.mediciones, key=lambda m: m.valor)
        return maximo.valor
    
    # Método para obtener la medicion minima
    def min_valor(self):
        minimo = min(self.mediciones,  key=lambda m: m.valor)
        return minimo.valor
    
    # Método para ver el resumen del sensor
    def ver_resumen(self):
        i = 1
        print(f" -- Sensor '{self.nombre_sensor}' --")
        for m in self.mediciones:
            print(f"Medicion {i}: {m.valor}")
            i += 1
        print(f" -- Resumen --\nValor máximo: {self.max_valor()} - Valor mínimo: {self.min_valor()} - Promedio: {self.promedio()}")