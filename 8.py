# operador logicos (and, or y not)
# and para que de si es verdadero o no, se tienen que cumplir las dos
# or para que te verdadero o no, vale con que solo uno cumpla
# not si niegas un valor verdadero lo convertira en falso, pero si tienes un valor falso lo convertira en verdadero

a = 10
b = 15
c = 20

resultado = not((a>b) and (b<c))
print(f"su resultado {resultado}")