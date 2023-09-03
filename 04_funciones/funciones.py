PI = 3.1416

def calcular_area(radio) :
    # 2.- area = PI * radio al cuadrado
    area = PI * (radio ** 2)
    # 3.- Imprimir area
    return area

def convertir_farenheit_a_celcius(grados_farenheit) :
    # 2.- grados_celcius = 5/9 * (grados_farenheit - 32)
    return (5/9 * (grados_farenheit - 32))

def main() :
    # 1.- Pedir radio
    radio = float(input("Escribe el radio: "))
    print(f"El área de un círculo de radio {radio} es: {calcular_area(radio)}")

    print(f"El área de un círculo de radio 10 es: {calcular_area(10)}")
    area = calcular_area(5)
    print(f"El área de un círculo de radio 5 es: {area}")

    # 1.- Pedir grados farenheit
    grados_farenheit = float(input("Escribe los grados Farenheit: "))
    print(f"{grados_farenheit} Farenheit son {convertir_farenheit_a_celcius(grados_farenheit)} Celcius")


main()

