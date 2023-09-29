def calcular_llenado(cantidad_ropa) :
    return (cantidad_ropa * 3)/10

def calcular_tiempo_lavado(cantidad_ropa) :
    tiempo_lavado = 0

    if cantidad_ropa <= 5 :
        tiempo_lavado = 15
    elif cantidad_ropa <= 10 :
        tiempo_lavado = 25
    else :
        tiempo_lavado = 35
    
    return tiempo_lavado + calcular_llenado(cantidad_ropa)

def calcular_tiempo_enjuague(cantidad_ropa) :
    tiempo_enjuague = 0

    if cantidad_ropa <= 5 :
        tiempo_enjuague = 10
    elif cantidad_ropa <= 10 :
        tiempo_enjuague = 15
    else :
        tiempo_enjuague = 20
    
    return tiempo_enjuague + calcular_llenado(cantidad_ropa)

def calcular_tiempo_secado(cantidad_ropa) :
    if cantidad_ropa <= 5 :
        return 5
    if cantidad_ropa <= 10 :
        return 10
    
    return 15


cantidad_ropa = float(input("Dime la cantidad de ropa: "))
lavar = input("Deseas lavar? ")
enjuagar = input("Deseas enjuagar? ")
secar = input("Deseas secar? ")

tiempo = 0
if cantidad_ropa <= 15 :
    if lavar == "s" :
        tiempo += calcular_tiempo_lavado(cantidad_ropa)
    if enjuagar == "s" :
        tiempo += calcular_tiempo_enjuague(cantidad_ropa)
    if secar == "s" :
        tiempo += calcular_tiempo_secado(cantidad_ropa)

    print(f"El tiempo total es: {tiempo}")
else :
    print("La cantidad de ropa excede el límite permitido")