"""
Desarrolla el algoritmo y posteriormente el programa 
completo en Python que solicite al usuario el valor 
asignado a los catetos de un triángulo rectángulo, y 
que calcule el valor resultante de la hipotenusa. Para 
la solución de este problema se sugiere que utilices el 
teorema de Pitágoras.

ENTRADAS
    cateto_a -> números
    cateto_b -> números
"""

# 1.- Pedir cateto A
cateto_a = float(input("Escribe el cateto A: "))
# 2.- Pedir cateto B
cateto_b = float(input("Escribe el cateto B: "))
# 3.- hipotenusa = raiz(cateto_a**2 + cateto_b**2)
hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
# 4.- imprimir hipotenusa
print(f"La hipotenusa es: {hipotenusa}")

"""
SALIDAS
    hipotenusa -> numero
"""
