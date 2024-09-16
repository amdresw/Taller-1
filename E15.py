#Ejercicio 15
#Enunciado:Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.
# Andrés Araque, grupo J1 
SalarioPre= int(input("Ingrese su salario: "))
PaisResidencia= str(input("Ingrese su país de residencia (País A, País B, País C): "))

match PaisResidencia:
    case "País A":
        impuestos = 0.20
    case "País B":
        impuestos = 0.15
    case "País C":
        impuestos = 0.10
    case _:
        impuestos = 0.25

 
salarioPost = SalarioPre * (1 - impuestos)#el 1 actúa como la base del 100% del salario bruto, al restar el porcentaje de impuestos obtenemos el porcentaje del salario que se retiene después de aplicar los impuestos.



print("Su salario neto después de impuestos es:",salarioPost)
