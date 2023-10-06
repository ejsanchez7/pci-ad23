"""
Inicia una matriz de 3 x 3 con los números del 1 al 9 
y la devuelve
"""
def inicia_matriz() :
    matriz = []
    contador = 1

    for i in range(3) :
        matriz.append([])
        for j in range(3) :
            matriz[i].append(contador)
            contador = contador + 1

    return matriz

"""
Imprime los valores de una matriz de cualquier tamaño
renglón por renglón con los valores separados por coma
"""
def imprime_matriz(matriz) :
    for i in range(len(matriz)) : # 0, 1, 2, 3
        for j in range(len(matriz[i])) : # 0, 1, 2
            print(matriz[i][j], end = ", ")
        print("")

"""
Suma los valores de dos matrices, A y B, del mismo tamaño
y los guarda en una matriz C que es devuelta
"""
def suma_matriz(matriz_a, matriz_b) :
    matriz_suma = []
    for i in range(len(matriz_a)) :
        matriz_suma.append([])
        for j in range(len(matriz_a[i])) :
            matriz_suma[i].append(matriz_a[i][j] + matriz_b[i][j])

    return matriz_suma            


matriz1 = [
    [5, 5, 5],
    [50, 60, 70],
    [100, 200, 300],
    [1, 2, 3]
]

matriz2 = [
    [5, 5, 5],
    [50, 60, 70],
    [100, 200, 300],
    [1, 2, 3]
]

suma = suma_matriz(matriz1, matriz2)
imprime_matriz(suma)