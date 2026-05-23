import matplotlib.pyplot as plt
import numpy as np

def graficar_recoleccion_vs_bateria(resultados: dict):
    nombres = list(resultados.keys())
    basura_total = [resultados[n]['basura_total'] for n in nombres]
    consumo_bateria = [resultados[n]['consumo_bateria'] for n in nombres]

    x = np.arange(len(nombres))
    ancho = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(x - ancho/2, basura_total,    ancho, label='Basura Recolectada', color='green')
    ax.bar(x + ancho/2, consumo_bateria, ancho, label='Batería Consumida',  color='red')

    ax.set_title('Rendimiento: Recolección vs Consumo Energético')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(x)
    ax.set_xticklabels(nombres)
    ax.legend()
    ax.grid(axis='y')

    plt.tight_layout()
    plt.show()
    