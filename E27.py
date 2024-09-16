#Ejercicio 27
#Enunciado: Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuarioadivinarlo.
# El programa debe dar pistas si el número ingresado es mayor o menor que el númerosecreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el número
# Andrés Araque

import random

Aleatorio = random.randint(1,100)

while True:
    num= int(input("Ingrese un número entre 1 y 100: \n"))
    if num == Aleatorio:
        print("Felicidades, adivinaste el número!")
        break #detener el cilo una vez se adivine el número correctamente.
    elif num < Aleatorio:
        print("El número es mayor, intenta nuevamente")
    else :
        print("El número es menor, intenta nuevamente")
print("Fin del juego")
