#Ejercicio 24
#Enunciado: Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i,o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.
#Andrés Araque, Grupo J1.

Cadena = input("Ingrese una cadena de texto: ")

ContadorVocales = 0

Vocales = "aeiou"

# Recorrer cada carácter en la cadena.
for Caracter in Cadena.lower():  # Convertir la cadena a minúsculas para evitar posibles errores por mayúsculas.
    if Caracter in Vocales:
        ContadorVocales += 1

print(f"La cadena contiene {ContadorVocales} vocales.")
