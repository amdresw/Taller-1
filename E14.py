#Ejercicio 14
#Enunciado: Escribe un programa que permita al usuario adivinar una letra secreta usando match .
# Andrés Araque, grupo J1

letraSecreta = "w"

letraUser = input("Adivina la letra secreta (en minúsculas): ")

match letraUser:
    case "w":
        print("Correcto, adivinaste.")
    case _: #el _ indica cualquier otro caracter que el usuario pueda ingresar.
        print("Incorrecto.")
