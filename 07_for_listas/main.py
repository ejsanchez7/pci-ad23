def imprime0_8() :
    for contador in range(9) :
        print(f"Número: {contador}")

def sumatoria(n) :
    suma = 0
    for contador in range(n + 1) :
        suma = suma + contador
    
    return suma

def sumatoria_while(n) :
    contador = 0
    suma = 0

    while contador <= n :
        suma = suma + contador
        contador = contador + 1
    
    return suma

def calcular_cociente(numerador, denominador) :
    division = 0
    resto = numerador

    while resto >= denominador :
        resto = resto - denominador
        division = division + 1
    
    return division, resto

def mostrar_pares(num) :
    for contador in range(2, num + 1, 2) :
        print(contador)

def mostrar_nones(num) :
    for contador in range(1, num + 1, 2) :
        print(contador)


# imprime0_8()
# print(f"La sumatoria es: {sumatoria(10)}")
# print(f"La sumatoria es: {sumatoria_while(10)}")
# print(calcular_cociente(15, 4))
mostrar_nones(15)