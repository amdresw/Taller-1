#ejercicio 11
#Enunciado: Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando match .
# Andrés Araque, grupo J1

Temperatura= int(input("Ingrese la temperatura a convertir: "))
Procedimiento= str(input("Selecione la opción del procedimiento que desea: \n 1) Convertir de Celsius a Fahrenheit \n 2) Convertir de Fahrenheit a Celsius \n "))

match Procedimiento:
    case "1":
        Procedimiento= (Temperatura*9/5)+32
        print (Procedimiento, "F")
    case "2":
        Procedimiento= (Temperatura -32)*5/9
        print (Procedimiento, "°")
