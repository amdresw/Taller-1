#Ejercicio 9
#Enunciado: Escribe un programa que clasifique a una persona en función de su edad.
# Andrés Araque, grupo J1

Edad = int(input("Ingrese su edad: "))

if Edad <= 0:
    print("Edad no válida")
elif 0 < Edad <= 12:
    print("Usted se encuentra en el grupo A, Niño (0-12 años)")
elif 13 <= Edad <= 17:
    print("Usted se encuentra en el grupo B, Adolescente (13-17 años)")
elif 18 <= Edad <= 64:
    print("Usted se encuentra en el grupo C, Adulto (18-64 años)")
elif Edad >= 65:
    print("Usted se encuentra en el grupo D, Anciano (65 o más años)")
