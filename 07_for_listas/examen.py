def cuenta_valores(lista) :
    rangos = [0, 0, 0, 0]

    for calificacion in lista :
        if calificacion <= 25 :
            rangos[0] = rangos[0] + 1
        elif calificacion <= 50 :
            rangos[1] = rangos[1] + 1
        elif calificacion <= 75 :
            rangos[2] = rangos[2] + 1
        else :
            rangos[3] = rangos[3] + 1

    return rangos

def histograma(lista) :
    for cantidad in lista :
        for index in range(cantidad) :
            print("*", end = "")
        print("")

def histograma2(lista) :
    for cantidad in lista :
        print("*" * cantidad)

lista1 = [14, 45, 83, 34, 98, 76]
rangos = cuenta_valores(lista1)
print(rangos)
histograma2(rangos)