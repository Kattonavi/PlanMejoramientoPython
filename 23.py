# ejercicio 4 calculadora aritmetica

# Solicitar al usuario dos números como números decimales
num1 = float(input("digite un numero"))
num2 = float(input("digite un numero"))

# Solicitar al usuario la operación a realizar (suma, resta, multiplicación o división)
operacion = input(" digite la operacion ").upper()

# Realizar la operación correspondiente según la opción seleccionada
if operacion=='S':
    suma = num1+num2
    print(f"la suma es {suma}")
    
elif operacion == 'R':
    resta = num1-num2
    print(f"la resta es {resta}")
    
elif operacion == 'M' or operacion == 'P':
    mult = num1*num2
    print(f"la multiplicacion es {mult:.2f}")
    
elif operacion == 'D':
    div = num1/num2
    print(f"la divicion es {div}")
    
else:
    print("se equivoco de operacion ")
    
