
import random

NumR= random.randint (1,10)

NumS= int (input("Intente adivinar un número de 1-10 \n"))

if (NumS>NumR) :
    print ("El numero ingresado es mayor, suerte la proxima ")
elif (NumS<NumR) :
    print ("El numero ingresado en menor, suerte la proxima")    
elif (NumS==NumR) :
    print("El numero ingresado es igual, felicidades") 
