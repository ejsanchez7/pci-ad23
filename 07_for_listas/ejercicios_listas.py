import math

def calcular_menor(lista) :
    menor = lista[0]

    for indice in range(1, len(lista)) :
        if menor > lista[indice] :
            menor = lista[indice]
    return menor

def calcular_promedio(lista) :
    suma = 0
    for elemento in lista :
        suma = suma + elemento
    
    return suma / len(lista)

def calcular_varianza(lista) :
    promedio = calcular_promedio(lista)
    suma = 0
    for numero in lista :
        suma = suma + (numero - promedio)
    
    return math.sqrt(suma / len(lista))


lista = [17, 28, 8, 5]

print(calcular_menor(lista)) # 8