#Ejercicio 9
#Clasificacion de edades

Edad= int(input("Ingrese su edad: "))
if (Edad <= 0 or Edad <= 12) :
    print("Usted se encuentra el grupo A, Niño (0-12 años)")
elif (Edad <= 13 or Edad <= 17) :
    print("Usted se encuentra el grupo B, Adolescente (13-17 años)")
elif (Edad <= 18 or Edad <= 64) :
    print("Usted se encuentra el grupo C, Adulto (18-64 años)")
elif (Edad>= 65 ) :
    print("Usted se encuentra el grupo D, Anciano (65 o más años)")
