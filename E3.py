#Ejercicio 3:
#Enunciado: Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match para realizar la operación correspondiente.
# Andrés Araque, grupo J1

Numero1= int ( input ("ingrese un numero: ")) 
Numero2= int  ( input ("ingrese un numero: ")) 
Operacion= str (input ("Selecione la operación: +, -, /, * \n  "))

match Operacion:

  case "+":
    Operacion= (Numero1+Numero2)
    print ("el resultado es=", Operacion)

  case "-":
    Operacion= (Numero1-Numero2)
    print ("el resultado es=", Operacion)

  case "/":
    Operacion= (Numero1/Numero2)
    print ("el resultado es=", Operacion)

  case "*":
    Operacion= (Numero1*Numero2)
    print ("el resultado es=", Operacion)  

        