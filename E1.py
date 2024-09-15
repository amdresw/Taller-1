#ejericio 1 
# Enunciado: Escribe un programa que verifique si un número es par o impar utilizando if .
# Andrés Araque, grupo J1
numero= int( input("ingrese un numero entero: "))
if numero %2==0 : #%2 divide el numero introducido en 2
 print(numero,"es par.")
else: 
 print(numero,"es impar.")