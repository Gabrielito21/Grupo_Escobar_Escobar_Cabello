from jugadores import Jugador, Defensa, Delantero, Mediocampista, Portero
import pandas as pd
import os
# Se define el país elegido:
pais_elegido = "Francia"

# Los jugadores seleccionados: 
# Arquero: Brice Samba
# Defensas: Malo Gusto, Lucas Digne, Dayot Upamecano, Jules Koundé
# Mediocampistas: Manu Koné, Michael Olise, N'Golo Kanté, Adrien Rabiot
# Delanteros: Kylian Mbappé, Ousmane Dembélé

jugadores_titulares = [
    Portero("Brice Samba", 32, 1.88, 1, atajadas = 73, goles_concedidos = 23),    #0

    Defensa("Malo Gusto", 23, 1.78, 2 , balones_recuperados = 34, autogoles = 0), #1
    Defensa("Lucas Digne", 32, 1.78, 3, balones_recuperados=24, autogoles=1),     #2
    Defensa("Dayot Upamecano", 27, 1.85, 4, balones_recuperados=27, autogoles=0), #3
    Defensa("Jules Koundé", 27, 1.80, 5, balones_recuperados=19, autogoles=2),    #4

    Mediocampista("Manu Koné", 25, 1.85, 6, asistencias=5, tarjetas_amarillas=2),       #5
    Mediocampista("Michael Olise", 24, 1.83, 11, asistencias=7, tarjetas_amarillas=4),  #6
    Mediocampista("N'Golo Kanté", 35, 1.68, 13, asistencias=3, tarjetas_amarillas=1),   #7
    Mediocampista("Adrien Rabiot", 31, 1.91, 14, asistencias=3, tarjetas_amarillas=3),  #8

    Delantero("Kylian Mbappé", 27, 1.78, 10, goles=25, penales=4), #9
    Delantero("Ousmane Dembélé", 29, 1.78, 7, goles=10, penales=1) #10
]

def simulador(jugadores_titulares):
    print("--- SIMULADOR DE CAMPEÓN DEL MUNDO ---")

    jugadores_titulares[5].correr()
    jugadores_titulares[2].marcar()

    jugadores_titulares[0].atajar()
    jugadores_titulares[0].saque_de_fondo()

    jugadores_titulares[3].barrer()
    jugadores_titulares[3].correr()
    jugadores_titulares[4].patear_pelota()

    jugadores_titulares[6].dar_pase()
    jugadores_titulares[7].saque_lateral()
    jugadores_titulares[5].falta()

    jugadores_titulares[9].correr()
    jugadores_titulares[9].driblar()
    jugadores_titulares[9].patear_al_arco()

    print(" ")
    print("Roles del Equipo:")
    for i in jugadores_titulares:
        i.mostrar_rol()

simulador(jugadores_titulares)

# Se crea el diccionario
datos_jugadores = []

for jugador in jugadores_titulares:

    datos = {
        "Pais": pais_elegido,
        "Dorsal": jugador.dorsal,
        "Nombre": jugador.nombre,
        "Edad": jugador.edad,
        "Altura_m": jugador.altura,
        "Posicion": jugador.__class__.__name__
    }
    if hasattr(jugador, "goles"):
        datos["Goles"] = jugador.goles

    if hasattr(jugador, "asistencias"):
        datos["Asistencias"] = jugador.asistencias

    if hasattr(jugador, "atajadas"):
        datos["Atajadas"] = jugador.atajadas

    if hasattr(jugador, "balones_recuperados"):
        datos["Balones_recuperados"] = jugador.balones_recuperados  

# Si el jugador posee esta estadística, se agrega al diccionario.
# En caso contrario, Pandas rellenará la columna con NaN.
    datos_jugadores.append(datos)

df = pd.DataFrame(datos_jugadores)
print("\n==============================")
print("TABLA DE LA SELECCIÓN")
print("==============================")
print(df)

print("\n==============================")
print("ESTADÍSTICAS")
print("==============================")

print(f"\nEdad promedio del equipo: {df['Edad'].mean():.2f} años")

print(f"Altura máxima del equipo: {df['Altura_m'].max():.2f} m")

print("\nCantidad de jugadores por posición:")
print(df["Posicion"].value_counts())


print("\nPromedio de edad por posición:")
print(df.groupby("Posicion")["Edad"].mean())

os.makedirs("output", exist_ok=True)


nombre_archivo = f"output/titulares_{pais_elegido.lower()}.csv"
df.to_csv(nombre_archivo, index=False)

print(f"\nArchivo CSV generado: {nombre_archivo}")