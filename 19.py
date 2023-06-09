# condicionales combinados
# Solicitar al usuario su edad como número entero
edad = int(input("digite su edad "))

# Comprobar si la edad está en el rango válido (mayor que 0 y menor que 100)
if 0<edad<100:
    print("edad correcta")
        # Comprobar si la edad es mayor o igual a 18 para determinar si es mayor de edad
    if edad >= 18:
        print("es mayor de edad")
else: 
    print("edad incorrecta")

