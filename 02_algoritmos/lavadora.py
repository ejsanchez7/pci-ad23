"""
ENTRADAS
    cantidad_ropa -> numero (decimal)
    lavar -> booleano (true/false)
    enjuagar -> booleano
    exprimir -> booleano
"""

# 1.- Pedir cantidad de ropa
cantidad_ropa = float(input("Escribe la cantidad de ropa: "))

# 2.- validar si la cantidad de ropa <= 15
if cantidad_ropa <= 15 :
    # 2.1.- Preguntar si se va a lavar
    lavar = input("¿Lavar? ")
    # 2.2.- Preguntar si se va a enjuagar
    enjuagar = input("¿Enjuagar? ")
    # 2.3.- Preguntar si se va a exprimir
    exprimir = input("Exprimir? ")
    tiempo_total = 0
    tiempo_carga = 3 * cantidad_ropa / 10

    # 2.4.- SI lavar  = "si"
    if lavar == "si" :
        # 2.4.1.- Sumar a total 25
        # 2.4.3.- Sumar a total el tiempo de carga
        # tiempo_total = tiempo_total + tiempo_carga
        tiempo_total += 25 + tiempo_carga
    # 2.5.- SI enjuagar = "si"
    if enjuagar == "si" :
        # 2.5.1.- Sumar a total 10
        # 2.5.3.- Sumar a total el tiempo de carga
        # tiempo_total = tiempo_total + tiempo_carga
        tiempo_total += 10 + tiempo_carga
    # 2.6.- SI exprimir = "si"
    if exprimir == "si" :
        # 2.6.1.- Sumar a total 10
        tiempo_total += 10
    #2.7.- Mostrar mensaje
    print(f"Tiempo total {tiempo_total} minutos")
else :
    # Mostrar mensaje de error
    print("La cantidad de ropa excede el límite de carga")

"""
SALIDAS
    mensaje -> cadena ("Tiempo total 50 minutos" | "La cantidad de ropa excede el límite de carga")
"""