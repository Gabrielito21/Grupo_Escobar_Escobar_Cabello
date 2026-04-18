import numpy as np
def calcular_movimiento(x,y, theta,v,omega,dt=0.1):
    np.clip(v, 0, 0.8)
    np.clip(omega, -0.6, 0.6)
    x_nuevo = x + v * np.cos(theta) * dt
    y_nuevo = y + v * np.sin(theta) * dt
    theta_nuevo = theta + omega * dt
    
    return x_nuevo, y_nuevo, theta_nuevo
def distancia_al_objetivo(x,y,x_meta,y_meta):
    distancia_euclidiana = np.sqrt((x_meta - x)**2 + (y_meta - y)**2)
    return distancia_euclidiana

def calcular_error_seguimiento(x_real,y_real,x_ideal,y_ideal):
    error = np.sqrt((x_ideal - x_real)**2 + (y_ideal - y_real)**2)
    return error