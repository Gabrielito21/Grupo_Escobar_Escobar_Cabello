from robot_base import RobotBase
import random


class RobotTresRuedas(RobotBase):
    def __init__(self, nombre, radio_rueda, capacidad_carga=20, x_inicial=0, y_inicial=0, yaw_inicial=0, ruedas_calibradas=False):
        super().__init__(nombre, capacidad_carga, x_inicial, y_inicial, yaw_inicial)
        self.__ruedas_calibradas = ruedas_calibradas
        self.__radio_rueda = radio_rueda

    def calibrar_giro(self):
        print(f" [{self.get_nombre()}] Calibrando triciclo con ruedas de {self.__radio_rueda} cm")
        self.__ruedas_calibradas = True

    def mover(self):
        reward, done = self.step(0.8, 0.2)
        return reward, done

    def limpiar(self):
        self._reducir_bateria(2.0)
        basura = random.uniform(0.5, 1.5)
        self._recolectar_basura(basura)


class RobotOruga(RobotBase):
    def __init__(self, nombre, capacidad_carga=50, x_inicial=0, y_inicial=0, yaw_inicial=0, tension_oruga=100):
        super().__init__(nombre, capacidad_carga, x_inicial, y_inicial, yaw_inicial)
        self.__tension_oruga = tension_oruga

    def ajustar_tension(self):  
        print(f" [{self.get_nombre()}] Ajustando la tension de la oruga a {self.__tension_oruga}%")

    def mover(self):
        reward, done = self.step(0.3, 0.8)
        return reward, done

    def limpiar(self):
        self._reducir_bateria(4.5)
        basura = random.uniform(2, 4)
        self._recolectar_basura(basura)


class RobotDron(RobotBase):
    def __init__(self, nombre, altura_maxima, capacidad_carga=5, x_inicial=0, y_inicial=0, yaw_inicial=0, en_vuelo=False):
        super().__init__(nombre, capacidad_carga, x_inicial, y_inicial, yaw_inicial)
        self.__altura_maxima = altura_maxima
        self.__en_vuelo = en_vuelo

    def despegar(self):
        print(f" [{self.get_nombre()}] Ha despegado y su altura maxima es de {self.__altura_maxima}")
        self.__en_vuelo = True

    def mover(self):
        if self.__en_vuelo:
            reward, done = self.step(2.5, 1)
            return reward, done
        else:
            return 0, False

    def limpiar(self):
        if self.__en_vuelo:
            self._reducir_bateria(3.0)
            basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(basura)