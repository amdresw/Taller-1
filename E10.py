#Ejercicio 10
#Enunciado:

Nota= int(input("ingrese su nota: "))

if (Nota <0 or Nota >100):
 print ("Invalida")

elif (Nota >= 90 or Nota >= 100 ) :
 print ("Usted obtuvo una A")
 
elif (Nota >= 80 or Nota >= 89 ) :
 print ("Usted obtuvo una B")

elif (Nota >= 70 or Nota >= 79 ) :
 print ("Usted obtuvo una C")

elif (Nota >= 60 or Nota >= 69 ) :
 print ("Usted obtuvo una D")

elif (Nota <60  ) :
 print ("Usted obtuvo una F")
