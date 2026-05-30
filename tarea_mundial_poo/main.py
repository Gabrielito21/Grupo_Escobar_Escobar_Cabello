from jugadores import Jugador, Defensa, Delantero, Mediocampista, Portero
import pandas as pd
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
