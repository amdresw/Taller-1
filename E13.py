#Ejercicio 13
#Enunciado:Escribe un programa que determine el mayor de tres números usando if .
# Andrés Araque, grupo J1 


numer1 = float(input("Ingrese el primer número: "))
numer2 = float(input("Ingrese el segundo número: "))
numer3 = float(input("Ingrese el tercer número: "))


if numer1 >= numer2 and numer1 >= numer3:
    print(f"El mayor número es: {numer1}")
elif numer2 >= numer1 and numer2 >= numer3:
    print(f"El mayor número es: {numer2}")
else:
    print(f"El mayor número es: {numer3}")
