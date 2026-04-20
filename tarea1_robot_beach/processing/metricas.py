import numpy as np
def calcular_IAE(errores,dt):
    IAE = np.sum(np.abs(errores)) * dt
    return IAE
def calcular_ISE(errores,dt):
    ISE = np.sum(errores**2) * dt
    return ISE
def calcular_ITAE(errores, dt):
    tiempos = np.arange(len(errores)) * dt
    ITAE = np.sum(tiempos * np.abs(errores)) * dt
    return ITAE
def calcular_ITSE(errores, dt):
    tiempos = np.arange(len(errores)) * dt
    ITSE = np.sum(tiempos * (errores**2)) * dt
    return ITSE
def calcular_todas_las_metricas(errores,dt):
    IAE = calcular_IAE(errores,dt)
    ISE = calcular_ISE(errores,dt)
    ITAE = calcular_ITAE(errores, dt)
    ITSE = calcular_ITSE(errores, dt)
    return round(IAE, 2), round(ISE, 2), round(ITAE, 2), round(ITSE, 2)
def calcular_mejora(valor_ppo,valor_mask):
    mejora = ((valor_ppo - valor_mask) / valor_ppo) * 100
    return mejora