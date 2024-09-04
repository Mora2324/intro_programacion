import random
import sys

numero_adivinar = random.randint(1,10)

numero = int(input("Ingrese un número para adivinar: "))
if numero > numero_adivinar:
        print("Te pasaste")
else:
    print("Te faltó")

while numero != numero_adivinar:
    numero = int(input("Ese no es, otra vez: "))
    if numero > numero_adivinar:
        print("Te pasaste")
    elif numero == numero_adivinar:
         print("Bien hecho!")
    else:
        print("Te faltó")