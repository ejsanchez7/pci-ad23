def cuenta_repeticiones(cadena, valor) :
    contador = 0
    for caracter in cadena :
        if caracter == valor :
            contador = contador + 1
    
    return contador


texto = "Esto es una prueba"

print(f'"{texto}" tiene {cuenta_repeticiones(texto, "u")} repeticiones de "u"') 