
# Se define la clase principal de "Jugador"
class Jugador:
    def __init__(self,nombre,edad,altura,dorsal):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal
    
    def correr(self):
        print(f"¡{self.nombre} está corriendo por la cancha!")

    def mostrar_rol(self):
        print(f"{self.nombre} - Jugador de fútbol.")
    # Métodos inventados:
    def patear_pelota(self):
        print(f"¡{self.nombre} pateó la pelota!")

    def falta(self):
        print(f"¡{self.nombre} hizo una falta!")

class Portero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, atajadas, goles_concedidos):
        super().__init__(nombre, edad, altura, dorsal)
        # Atributos propios
        self.atajadas = atajadas
        self.goles_concedidos = goles_concedidos

    def mostrar_rol(self):
        print(f"{self.nombre} - Portero.")
    # Métodos propios
    def atajar(self):
        print(f"¡{self.nombre} atajó la pelota!")

    def saque_de_fondo(self):
        print(f"{self.nombre} sacó desde el fondo.")

class Defensa(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, autogoles):
        super().__init__(nombre, edad, altura, dorsal)
        # Atributos propios
        self.balones_recuperados = balones_recuperados
        self.autogoles = autogoles

    def mostrar_rol(self):
        print(f"{self.nombre} - Defensa.")
    # Métodos propios
    def barrer(self):
        print(f"¡{self.nombre} barrió a un contrincante!")

    def marcar(self):
        print(f"{self.nombre} marcó a un contrincante.")

class Mediocampista(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, asistencias, tarjetas_amarillas):
        super().__init__(nombre, edad, altura, dorsal)
        # Atributos propios
        self.asistencias = asistencias
        self.tarjetas_amarillas = tarjetas_amarillas

    def mostrar_rol(self):
        print(f"{self.nombre} - Mediocampista.")
    # Métodos propios
    def dar_pase(self):
        print(f"{self.nombre} dió un pase.")

    def saque_lateral(self):
        print(f"{self.nombre} sacó desde un lateral.")

class Delantero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, goles, penales):
        super().__init__(nombre, edad, altura, dorsal)
        # Atributos propios
        self.goles = goles
        self.penales = penales

    def mostrar_rol(self):
        print(f"{self.nombre} - Delantero.")
    # Métodos propios
    def patear_al_arco(self):
        print(f"¡{self.nombre} pateó al arco!")
    
    def driblar(self):
        print(f"{self.nombre} está driblando.")