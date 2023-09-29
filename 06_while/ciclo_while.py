def f1(n) :
    contador = 1
    suma = 0

    while contador <= n :
        suma += contador
        contador += 1

    return suma

def menu() :

    continua = True

    while continua :
        print("1.- Imprimir mensaje")
        print("2.- Salir")
        opcion = int(input("Selecciona una opción -> "))

        if opcion == 2 :
            continua = False
        if opcion == 1 :
            print("Hola")


# print(f"La sumatoria de 7 es: {f1(7)}")
menu()

