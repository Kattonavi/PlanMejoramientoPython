# ejercicio 5
# una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente

# Solicitar al usuario el precio como número decimal
precio = float(input(" digite el precio "))

# Calcular el descuento aplicando un 15% sobre el precio
descuento = precio * 0.15

# Calcular el precio final restando el descuento al precio original
preccio_final = precio - descuento

# Imprimir el valor final a pagar con dos decimales de precisión
print(f"el valor final a pagar es ${preccio_final:.2f}")
