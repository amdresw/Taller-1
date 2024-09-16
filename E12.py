#Ejercicio 12
#Enunciado: Escribe un programa que calcule el IMC y determine el estado de peso.
# Andrés Araque, grupo J1 

Peso = float(input("Ingrese su peso (kg): \n"))
Altura = float(input("Ingrese su altura (m): \n"))

Imc = Peso / (Altura ** 2)
Imc = round(Imc, 2)  # Redondea a 2 decimales

if Imc > 30:
    print(Imc, "Usted tiene obesidad")
elif 25 <= Imc <= 29.9:
    print(Imc, "Usted tiene sobrepeso")
elif 18.5 <= Imc <= 24.9:
    print(Imc, "Usted tiene un peso normal")
elif Imc < 18.5:
    print(Imc, "Usted tiene un peso bajo")