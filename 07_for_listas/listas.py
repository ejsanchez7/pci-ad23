def suma8(lista) :
    lista[0] = lista[0] + 8
    lista[1] = lista[1] + 8
    lista[2] = lista[2] + 8

    return lista

def suma8_reloaded(lista) :
    for indice in range(len(lista)) :
        lista[indice] = lista[indice] + 8
    
    return lista

def promediar(lista) :
    suma = 0
    for numero in lista :
        suma = suma + numero
    
    return suma/len(lista)

def crea_lista(tam, valor) :
    lista = []
    for indice in range(tam) :
        lista.append(valor)
    return lista

def crea_lista_input(tam) :
    lista = []
    for indice in range(tam) :
        valor = int(input("Escribe el valor: "))
        lista.append(valor)
    return lista


lista = [4, 56, 83]

#print(suma8(lista))
#print(suma8_reloaded(lista))
#print(promediar(lista))
#print(crea_lista(5, 100))
#print(crea_lista_input(5))

lista2 = []
cantidad = int(input("Escribe la cantidad de numeros: "))

for indice in range(cantidad) :
    valor = int(input(f"Escribe el número {indice + 1}: "))
    lista2.append(valor)

print(f"El promedio es: {promediar(lista2)}")
