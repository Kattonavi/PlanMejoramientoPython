# ejercicio 1 numeros pares e impares

# Solicitar al usuario dos números enteros
num1 = int(input("digite un numero "))
num2 = int(input("digite otro numero "))

# Comprobar si ambos números son pares
if num1%2==0 and num2%2==0:
    print("ambos numeros son pares")

# Comprobar si el primer número es par y el segundo número es impar
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par ")
    
# Comprobar si el primer número es impar y el segundo número es par
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par ")
    
# Si no se cumple ninguna de las condiciones anteriores, entonces ambos números son impares
else:
    print("ambos numeros son impares")