from robot_base import RobotBase
import random


class RobotTresRuedas(RobotBase):
    def _init_(self, nombre, radio_rueda, capacidad_carga=20, x_inicial=0, y_inicial=0, yaw_inicial=0, ruedas_calibradas=False):
        super()._init_(nombre, capacidad_carga, x_inicial, y_inicial, yaw_inicial)
        self.__ruedas_calibradas = ruedas_calibradas
        self.__radio_rueda = radio_rueda

    def calibrar_giro(self):
        print("Se ha calibrado el giro del robot de tres ruedas")
        self.__ruedas_calibradas = True
    

    def mover(self, v, w):
        
        reward, done = self.step(0.8, 0.2)
        return reward, done

    def limpiar(self):
        self._gastar_bateria(2.0)
        basura = random.uniform(0.5, 1.5)
        self._recolectar_basura(basura)


class RobotOruga(RobotBase):
    def _init_(self, nombre, tension_oruga, capacidad_carga=50, x_inicial=0, y_inicial=0, yaw_inicial=0):
        super()._init_(nombre, capacidad_carga, x_inicial, y_inicial, yaw_inicial)
        self.__tension_oruga = tension_oruga

    def ajustar_tension(self):
        print("Se ha ajustado la tensión de las orugas")
        self.__tension_oruga = tension_oruga

    def mover(self, v, w):
        reward, done = self.step(0.3, 0.8)
        return reward, done

    def limpiar(self):
        self._gastar_bateria(4.5)
        basura = random.uniform(2, 4)
        self._recolectar_basura(basura)


class RobotDron(RobotBase):
    def _init_(self, nombre, altura_maxima, capacidad_carga=5, x_inicial=0, y_inicial=0, yaw_inicial=0, en_vuelo=False):
        super()._init_(nombre, capacidad_carga, x_inicial, y_inicial, yaw_inicial)
        self.__altura_maxima = altura_maxima
        self.__en_vuelo = en_vuelo

    def despegar(self):
        print(f"el dron  ha despegado y su altura máxima es de {self.__altura_maxima}")
        self.__en_vuelo = True

    def mover(self, v, w):
        if self.__en_vuelo == True:
            reward, done = self.step(2.5, 1)
            return reward, done
        else:
            return 0, False

    def limpiar(self):
        if self.__en_vuelo==True:
            self._gastar_bateria(3.0)
            basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(basura)
            
