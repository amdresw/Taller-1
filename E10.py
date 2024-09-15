#Ejercicio 10
#Enunciado: Escribe un programa que asigne una calificación basada en una nota numérica.
# Andrés Araque, grupo J1

Nota = int(input("Ingrese su nota: "))

if Nota < 0 or Nota > 100:
    print("Invalida")

elif 90 <= Nota <= 100:
    print("Usted obtuvo una A")

elif 80 <= Nota <= 89:
    print("Usted obtuvo una B")

elif 70 <= Nota <= 79:
    print("Usted obtuvo una C")

elif 60 <= Nota <= 69:
    print("Usted obtuvo una D")

elif Nota < 60:
    print("Usted obtuvo una F")
