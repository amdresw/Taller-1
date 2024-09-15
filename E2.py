#Ejercicio 2 
#Enunciado: Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando if .

calificacion= int( input ("ingrese una calificación: ") )
if (calificacion <0 or calificacion >100):
 print ("Invalida")
elif (0< calificacion <60):
  print ("Desaprodabo")
elif (60<=calificacion<=100) :
  print ("Aprobado")