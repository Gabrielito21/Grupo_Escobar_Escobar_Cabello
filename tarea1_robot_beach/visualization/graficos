import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
def plot_metricas(diccionario_experimentos, ambiente, ruta):
    exp_PPO = None    
    exp_PPO_mask = None   
    
    for nombre_exp, detalles in diccionario_experimentos.items():
        if detalles["ambiente"] == ambiente and detalles["ruta"] == ruta:
            if detalles["politica"] == "PPO":
                exp_PPO = detalles
            elif detalles["politica"] == "PPO-Mask":
                exp_PPO_mask = detalles
    
    if exp_PPO is None or exp_PPO_mask is None:
        print(f"No se encontraron experimentos para el ambiente '{ambiente}' y ruta '{ruta}'.")
        return

    plt.figure(figsize=(20, 5))
    nombres = ["PPO", "PPO-Mask"]
     
    
    plt.subplot(1, 4, 1)
    valores_ise = [exp_PPO["ISE"], exp_PPO_mask["ISE"]]
    plt.bar(nombres, valores_ise, color=['blue', 'orange'])
    plt.title("ISE")

    
    plt.subplot(1, 4, 2)
    valores_iae = [exp_PPO["IAE"], exp_PPO_mask["IAE"]]
    plt.bar(nombres, valores_iae, color=['blue', 'orange'])
    plt.title("IAE")

    
    plt.subplot(1, 4, 3)
    valores_itse = [exp_PPO["ITSE"], exp_PPO_mask["ITSE"]]
    plt.bar(nombres, valores_itse, color=['blue', 'orange'])
    plt.title("ITSE")

    
    plt.subplot(1, 4, 4)
    valores_itae = [exp_PPO["ITAE"], exp_PPO_mask["ITAE"]]
    plt.bar(nombres, valores_itae, color=['blue', 'orange'])
    plt.title("ITAE")

    plt.tight_layout()
    
   
    if not os.path.exists("resultados_graficos"):
        os.makedirs("resultados_graficos")

    nombre_archivo = f"metricas_{ambiente}_{ruta}.png"
    ruta_final = os.path.join("resultados_graficos", nombre_archivo)
    plt.savefig(ruta_final, dpi=300)
    plt.show()

#  Gráfico de LiDAR 
def plot_lidar(angulos, distancias, distancias_norm):
    plt.figure(figsize=(12, 6))
    

    plt.subplot(1, 2, 1)
    plt.scatter(angulos, distancias, color='blue', s=10) 
    plt.title("Lectura de LiDAR (Distancias Reales)")
    plt.xlabel("Ángulo (grados)")
    plt.ylabel("Distancia [m]")


    plt.subplot(1, 2, 2)
    plt.plot(angulos, distancias_norm, color='orange')
    plt.title("Lectura de LiDAR (Vector IA)")
    plt.xlabel("Ángulo (grados)")
    plt.ylabel("Distancia Normalizada")

    plt.tight_layout()
    
    if not os.path.exists("resultados_graficos"):
        os.makedirs("resultados_graficos")
        
    ruta_final = os.path.join("resultados_graficos", "lidar.png")
    plt.savefig(ruta_final, dpi=300)
    plt.show()

#  Gráfico de Trayectorias
def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    plt.figure(figsize=(10, 10)) 
    

    plt.plot(x_ppo, y_ppo, label="PPO", color='blue', alpha=0.7)
    plt.plot(x_mask, y_mask, label="PPO-Mask", color='orange', alpha=0.7)
    
    waypoints = np.array(waypoints)
    plt.scatter(waypoints[:, 0], waypoints[:, 1], color='black', s=100, marker='s', label="Waypoints")
    plt.axis('equal') 
    
    plt.title(f"Trayectorias - {nombre}")
    plt.xlabel("X [m]")
    plt.ylabel("Y [m]")
    plt.legend()
    
    if not os.path.exists("resultados_graficos"):
        os.makedirs("resultados_graficos")
        
    nombre_archivo = f"trayectorias_{nombre}.png"
    ruta_final = os.path.join("resultados_graficos", nombre_archivo)
    plt.savefig(ruta_final, dpi=300)
    plt.show()