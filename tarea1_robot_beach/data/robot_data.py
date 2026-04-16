import numpy as np
# Estructura de datos del proyecto:

# De las tablas 6, 7 , 8:

def cargar_experimentos():
    experimentos ={
        # Tabla 6:
        "exp1": {
            "politica": "PPO",
            "ambiente": "real", 
            "ruta": "simple",
            "ISE": 434.99,
            "IAE": 135.93,
            "ITSE": 6932.79,
            "ITAE": 2601.61, 
            "tiempo_s": None,
            "pasos": None, 
            "reward_medio": None,
        },

        "exp2": {
            "politica": "PPO-Mask",
            "ambiente": "real", 
            "ruta": "simple",
            "ISE": 362.85,
            "IAE": 128.92,
            "ITSE": 5869.30,
            "ITAE": 2669.86, 
            "tiempo_s": None,
            "pasos": None, 
            "reward_medio": None,
        },
        "exp3": {
            "politica": "PPO",
            "ambiente": "simulado", 
            "ruta": "simple",
            "ISE": 73.35,
            "IAE": 24.51,
            "ITSE": 203.90,
            "ITAE": 89.73, 
            "tiempo_s": None,
            "pasos": None, 
            "reward_medio": None,
        },
        "exp4": {
            "politica": "PPO-Mask",
            "ambiente": "simulado", 
            "ruta": "simple",
            "ISE": 73.79,
            "IAE": 22.91,
            "ITSE": 200.16,
            "ITAE": 73.77, 
            "tiempo_s": None,
            "pasos": None, 
            "reward_medio": None,
        },
        # Tabla 7:
        "exp5": {
            "politica": "PPO",
            "ambiente": "simulado", 
            "ruta": "cuadrado",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None, 
            "tiempo_s": 27.89,
            "pasos": 270, 
            "reward_medio": 7.12,
        },        
        "exp6": {
            "politica": "PPO",
            "ambiente": "real", 
            "ruta": "cuadrado",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None, 
            "tiempo_s": 112,
            "pasos": 270, 
            "reward_medio": 7.12,
        },        
    }

    return experimentos

def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100):
    x_ideal = []
    y_ideal = []
    
    for i in range(len(waypoints) - 1):
        x0, y0 = waypoints[i]
        x1, y1 = waypoints[i + 1]
        
        x_segmento = np.linspace(x0, x1, puntos_por_segmento)
        y_segmento = np.linspace(y0, y1, puntos_por_segmento)
        
        x_ideal.extend(x_segmento)
        y_ideal.extend(y_segmento)
    
    return np.array(x_ideal), np.array(y_ideal)
print

