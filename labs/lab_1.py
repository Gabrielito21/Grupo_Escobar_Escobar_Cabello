#Integrantes
#   1. Gabriel Escobar 
#   2. Felipe Escobar 
#   3. Benjamin cabello 

# ejercicio 1 
v= int(input("Ingrese valor voltaje: "))
i = int(input("Ingrese valor corriente: "))
r= v/i
p= v*i

print("El valor de la resistencia es: ",r)
print("El valor de la potencia es:  ",p)
if p > 1000 :
    print("¡Peligro! Alta disipación de potencia detectada.")
else:
    print("Operación en rangos seguros.")

 # ejercicio 2 
vi= int(input("Ingrese voltaje inicial: "))  
vi_min= int(input("El voltaje minimo es: "))
h=0
while vi>vi_min:
    vi=vi*0.97
    h=+1
print("La cantidad de horas que cayo el banco de baterias fue: ",h)

#ejercicio 3

miau=0
while miau!= 4 :
 print("1. Convertir miliamperios (mA) a amperios (A).")
 print("2. Convertir microfaradios (µF) a faradios (F).")
 print("3. Convertir kiloohmios (kΩ) a ohmios (Ω).")
 print("4. Salir")
 miau=int(input("Ingrese opcion deseada: "))
 if miau==1 :
    amper=int(input("Ingrese corriente en mili: "))
    amper1=amper*0.001
    print("Ampere: ",amper1)
 elif miau==2:
    fara=int(input("Ingrese faradios en micro: "))
    fara1=fara*0.000001
    print("Faradios: ",fara1)
 elif miau==3:
    ohm=int(input("Ingrese ohm en kilo: "))
    ohm1=ohm*100
    print("Ohm: ",ohm1)
 elif miau == 4:
    break
 else :
    print("error")
# Ejercicio 4
 rackOn = True
 while rackOn:
    temp = int(input("Ingrese temperatura en °C: "))
    if temp >= 20 and temp <= 40:
       print("Estado Normal")
    elif temp >40 and temp <=75:
       print("Advertencia: Encendiendo ventiladores auxiliares")
    elif temp >75:
       print("¡Peligro Crítico! Apagando servidor de emergencia")
       rackOn = False
       break
    else:
       print("Valor de temperatura inválido o muy bajo")



