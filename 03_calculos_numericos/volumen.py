"""
Desarrolla el algoritmo y posteriormente un programa completo en 
Python que determine el volumen de la siguiente figura geométrica 
(imagine que es un medio cilindro). El radio (r) y la altura (h) 
son solicitadas al usuario.
ENTRADAS:
    radio -> numero
    altura -> numero
"""
import math

# 1.- Pedir radio
radio = float(input("Escribe el radio: "))
# 2.- Pedir altura
altura = float(input("Escribe la altura: "))
# 3.- volumen = PI * radio**2 * h / 2
volumen = (math.pi * radio ** 2 * altura) / 2
# 4.- Imprimir volumen
print(f"El volumen es: {volumen}")

"""
SALIDAS
    volumen -> numero
"""
