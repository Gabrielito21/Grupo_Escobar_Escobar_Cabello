#Integrantes
#   1. Gabriel Escobar 
#   2. Felipe Escobar 
#   3. Benjamin cabello 
# Ejercicio 1: Calculadora ley de Ohm.
v = int(input("Ingrese el valor de Voltaje: "))
i = int(input("Ingrese el valor de Corriente: "))
if i != 0:
    p = v * i
    r = v/i
    print("Resistencia: ", r)
    print("Potencia: ", p)
    if p >= 1000:
        print("¡Peligro! Alta disipación de potencia detectada.")
    else:
        print("Operación en rangos seguros")
else: 
    print("Valor de corriente inválido")
