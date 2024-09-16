#Ejercicio 5
#Enunciado: Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la semana usando match .
# Andrés Araque, grupo J1

Numero = input("Ingrese un número del 1 al 7: \n")

#Mejora en la sintaxis usando match
match Numero:

    case "1":
        print("Hoy es Lunes")
    case "2":
        print("Hoy es Martes")
    case "3":
        print("Hoy es Miércoles")
    case "4":
        print("Hoy es Jueves")
    case "5":
        print("Hoy es Viernes")
    case "6":
        print("Hoy es Sábado")
    case "7":
        print("Hoy es Domingo")
    case _:
        print("Número no válido. Por favor, ingrese un número del 1 al 7.")

  
  



