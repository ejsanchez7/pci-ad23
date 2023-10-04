"""
Ejercicios de clase en:
https://www.alphagrader.com/courses/59/assignments/615
"""

def muestra_menu() :
    opciones = [
        "Crea lista",
        "Inicializa lista",
        "Cuenta impares",
        "Invierte lista",
        "Mayor",
        "Salir"
    ]

    for indice in range(len(opciones)) :
        print(f"{indice + 1}.- {opciones[indice]}")

"""
recibe el tamaños de la lista a crear. La función deberá pedir un valor
numérico al usuario para cada casilla de la lista y al final devolver 
la lista creada.
"""
def crea_lista(tam) :
    lista = []
    for indice in range(tam) :
        valor = int(input(f"Valor{indice + 1} es: "))
        lista.append(valor)

    return lista

"""
recibe una lista y un valor por default. La función cambia todos los valores
de la lista al valor por default. La función no crea una nueva lista, sino 
que modifica la que recibe como parámetro.Para mandar a llamar esta función 
antes de debes de usar crea_lista para asegurarte que tienes valores que contar.
"""
def inicializa_lista(lista, valor) :
    for indice in range(len(lista)) :
        lista[indice] = valor

"""
recibe una lista y regresa la cantidad de elementos impares en ella. Para mandar
a llamar esta función antes de debes de usar crea_lista para asegurarte que tienes
valores que contar.
"""
def cuenta_impares(lista) :
    cuenta = 0
    for numero in lista :
        if numero % 2 != 0 :
            cuenta = cuenta + 1
    
    return cuenta

"""
recibe una lista y la modifica para que sus elementos esten en el orden inverso. 
Haz usos de un variable auxiliar, pero no de una segunda lista. Para mandar a llamar 
esta función antes de debes de usar crea_lista para asegurarte que tienes valores que contar
"""
def invierte_lista(lista) :
    indice_invertido = len(lista) - 1
    indice = 0

    while indice < indice_invertido :
        auxiliar = lista[indice]
        lista[indice] = lista[indice_invertido]
        lista[indice_invertido] = auxiliar
        indice = indice + 1
        indice_invertido = indice_invertido - 1


"""
recibe una lista de números y devulve el valor más grande en la lista. Para mandar
a llamar esta función antes de debes de usar crea_lista para asegurarte que tienes 
valores que contar.
"""
def mayor_valor(lista) :
    mayor = lista[0]

    for indice in range(1, len(lista)) :
        if lista[indice] > mayor :
            mayor = lista[indice]
    
    return mayor

while True :

    muestra_menu()
    seleccion = int(input("Selecciona una opción --> "))
    print("\n")

    if seleccion == 1 :
        tam = int(input("Escribe el tamaño de la lista a crear: "))
        print(crea_lista(tam))
    elif seleccion == 2 :
        tam = int(input("Escribe el tamaño de la lista a crear: "))
        lista = crea_lista(tam)
        valor = int(input("Escribe el valor con el que se inicializará la lista: "))
        inicializa_lista(lista, valor)
        print(lista)
    elif seleccion == 3 :
        tam = int(input("Escribe el tamaño de la lista a crear: "))
        lista = crea_lista(tam)
        print(f"Hay {cuenta_impares(lista)} números impares en la lista")
    elif seleccion == 4 :
        tam = int(input("Escribe el tamaño de la lista a crear: "))
        lista = crea_lista(tam)
        print(lista)
        invierte_lista(lista)
        print(lista)
    elif seleccion == 5 :
        tam = int(input("Escribe el tamaño de la lista a crear: "))
        lista = crea_lista(tam)
        print(f"El mayor en la lista es {mayor_valor(lista)}")
    elif seleccion == 6 :
        print("Adiós!")
        break
    else :
        print("Entrada no válida")
    
    print("\n")
