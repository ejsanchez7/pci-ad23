"""
Un algoritmo que transforme grados Farenheit a Celsius. 
Recuerda que Celsius = 5 / 9 ( Farenheit - 32).

ENTRADAS
    grados_farenheit -> numero
"""

# 1.- Pedir grados farenheit
grados_farenheit = float(input("Escribe los grados Farenheit: "))
# 2.- grados_celcius = 5/9 * (grados_farenheit - 32)
grados_celcius = 5/9 * (grados_farenheit - 32)
# 3.- imprimir grados_celcius
print(f"{grados_farenheit} Farenheit son {grados_celcius} Celcius")

"""
SALIDAS
    grados_celcius -> numero
"""
