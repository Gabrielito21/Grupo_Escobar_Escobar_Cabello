class PistaAudio :
    plataforma = 'Spotify'
    def __init__(self, titulo, duracion):
        self.titulo=titulo
        self.duracion=duracion
    
#Metodo estatico
    def formatear_tiempo(segundos):
        minutos = segundos // 60
        seg_restantes = segundos %60
        return f"{minutos}:{seg_restantes:02d}"

class Cancion(PistaAudio):
    def __init__(self, titulo, duracion, artista, genero):
        super().__init__(titulo, duracion)
        self.artista = artista
        self.genero = genero
    
    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de '{self.artista}' genero '{self.genero}' en '{self.plataforma}'")

mi_cancion = Cancion("The Best", 238, "Conan Gray", "Pop")

# Usamos el método estático para formatear los 238 segundos
tiempo_str = PistaAudio.formatear_tiempo(mi_cancion.duracion)
print(f"Duración de la canción: {tiempo_str}")

# Ejecutamos la reproducción
mi_cancion.reproducir()




