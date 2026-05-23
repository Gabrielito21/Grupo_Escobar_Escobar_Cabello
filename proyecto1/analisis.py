import numpy as np
def comparar_rendimiento(datos: list) -> dict:
     matriz1 = np.array(datos, dtype=object)
     nombres_unicos=np.unique(matriz1[:,1])
     resultados={}
     for nombre in nombres_unicos:

        filtro = matriz1[:, 1] == nombre
        datos_robot = matriz1[filtro]

        bateria = datos_robot[:, 4].astype(float)
        basura_recolectada = datos_robot[:, 5].astype(float)

        consumo_bateria = 100.0 - bateria[-1]

        basura_total = basura_recolectada[-1]

        if consumo_bateria == 0:
            eficiencia = 0.0
        else:
            eficiencia = basura_total / consumo_bateria

        resultados[nombre] = {
            'consumo_bateria': consumo_bateria,
            'basura_total': basura_total,
            'eficiencia': eficiencia
        }

     return resultados