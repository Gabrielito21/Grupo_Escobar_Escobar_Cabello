class Sensor:
   def medir(self):
      print("Midiendo datos base...")

class SensorTemperatura(Sensor):
    def medir(self):
        print("Midiendo temperatura en grados Celsius")

class SensorLuz(Sensor):
    def medir(self):
        print("Midiendo nivel de luz en Lux")

def iniciar_medicion(sensor_cualquiera):
    sensor_cualquiera.medir()

sensor_temp = SensorTemperatura()
sensor_luz = SensorLuz()
sensor_x = Sensor()

print(" Prueba 1 ")
iniciar_medicion(sensor_x)

print("\n Prueba 2 ")
iniciar_medicion(sensor_luz)

print("\n Prueba 3 (Sensor Base) ")
iniciar_medicion(sensor_temp)