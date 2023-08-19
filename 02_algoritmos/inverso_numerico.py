num = int(input("Escribe el número a invertir: "))
inverted = 0

while num >= 10 :
    remainder = num % 10
    num = num // 10
    inverted = (inverted * 10) + remainder

inverted = (inverted * 10) + num

print(f"El inverso es: {inverted}")