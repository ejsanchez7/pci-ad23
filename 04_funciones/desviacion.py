import math

def promedio(num1, num2, num3) :
    return (num1 + num2 + num3)/3

def desviacion(num1, num2, num3) :
    prom = promedio(num1, num2, num3)
    suma = math.pow((num1 - prom), 2) + math.pow((num2 - prom), 2) + math.pow((num3 - prom), 2)
    return math.sqrt(suma/2)

print(f"Desviación estándar de 20, 30, 40 = {desviacion(20, 30, 40)}")