#Ejercicio 4
#Enunciado: Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el triángulo es equilátero, isósceles o escaleno.
# Andrés Araque, grupo J1

Lado1= int(input("Ingrese un lado del triángulo: "))
Lado2= int(input("Ingrese el siguiente lado del triángulo: "))
Lado3= int(input("Ingrese el último lado del triángulo: "))

if Lado1==Lado2==Lado3 :
    print("el triángulo es: equilátero")

elif (Lado1==Lado2 or Lado1==Lado3 or Lado2==Lado3 ) :
    print("el triángulo es: isóceles")  
   
else:
    print("El triángulo es: escaleno ")
    
