# def obtener_mayor(num1, num2) :
#     if num1 > num2 :
#         return num1
#     elif num2 > num1 :
#         return num2
#     else:
#         return None

def obtener_mayor(num1, num2) :
    mayor = num1
    if num1 < num2 :
        mayor = num2
    elif num2 == num1 :
        mayor = None
        
    return mayor