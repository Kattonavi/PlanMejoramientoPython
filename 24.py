# ejercicio 5 menu de opciones
# 1 ingresar dinero en la cuenta
# 2 retirar dinero de la cuenta
# 3 mostrar dinero disponible
# salir

saldo = 1000

print("\t.:MENU:.")
print("1. ingresar dinero en la cuenta")
print("2. retirar dinero de la cuenta")
print("3. mostrar dinero disponible")
print("4. salir")
opcion = int(input("digite una opcion de menu "))

print()

if opcion==1:
    extra = float(input("cuanto dinero desea retirar "))
    saldo += extra
    print(f"dinero de la cuenta {saldo}")
elif opcion == 2:
    retirar = float(input("cuanto dinero desea retirar"))
    if retirar>saldo:
        print("no tiene esa cantidad de dinero")
    else:
        saldo -= retirar
        print(f"dinero de la cuenta {saldo}")
elif opcion == 3:
    print(f"dinero de la cuenta {saldo}")
elif opcion == 4:
    print("gracias por utilizar su cajero de confianza automatico")
else:
    print("error, se equivoco de opcion de menu")