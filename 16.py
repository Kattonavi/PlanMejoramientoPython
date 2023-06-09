# area y longitud de un circulo ejercicio 4

import math

# Solicitar al usuario el valor del radio como número decimal
radio = float(input("digite el radio "))

# Calcular el área y la longitud del círculo utilizando la fórmula matemática correspondiente
area = math.pi * radio**2
longitud = 2 * math.pi * radio

# Imprimir el área y la longitud con dos decimales de precisión
print(f"el area es {area:.2f} ")
print(f"la longitud es {longitud:.2f} ")
