#Ejercicio 22
#Enunciado: Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos internos usando if .
# Andres Araque, Grupo J1.

Angulo1 = float(input("Ingrese el primer ángulo del triángulo (en grados): "))
Angulo2 = float(input("Ingrese el segundo ángulo del triángulo (en grados): "))
Angulo3 = float(input("Ingrese el tercer ángulo del triángulo (en grados): "))


if Angulo1 + Angulo2 + Angulo3 != 180:
    print("Los ángulos no forman un triángulo válido.")
else:
    # Clasificación
    if Angulo1 == 90 or Angulo2 == 90 or Angulo3 == 90:
        Tipo = "Rectángulo"
    elif Angulo1 > 90 or Angulo2 > 90 or Angulo3 > 90:
        Tipo = "Obtuso"
    else:
        Tipo = "Agudo"
    
    print(f"El triángulo es {Tipo}.")
