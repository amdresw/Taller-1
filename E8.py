#ejercicio 8
#Enunciado: año bisiesto
año= int(input("Ingrese un año:\n ")) 

if (año % 4 == 0 and año % 100 !=0 ) or (año % 400 == 0 ) :
    print("El año es bisiesto")

else:
    print("El año no es bisiesto")
