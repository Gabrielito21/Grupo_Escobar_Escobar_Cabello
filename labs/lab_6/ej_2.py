#ejercicio 2
class instrumento :
    def __init__(self, marca):
        self.marca = marca
        self.estado = "apagado"
    def escender(self):
        self.estado = "encendido"
        print(f"El instrumento {self.marca} está encendido.") 
    def validar_voltaje(voltaje):
        if voltaje < 0 or voltaje > 220:
          return voltaje
class osicolscopio(instrumento):
    def __init__(self, marca, canales):
        super().__init__(marca)
        self.canales = canales
    def medir_señal(self):
        if self.estado == "apagado":
            print("El osciloscopio está apagado. Por favor, enciéndelo para medir la señal.")
        else:
            print(f"Midiendo señal en {self.canales} canales con el osciloscopio {self.marca}.")

probar= osicolscopio("Tektronix", 2)
probar.medir_señal()
probar.escender()
probar.medir_señal()   