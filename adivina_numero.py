import random

numero = random.randrange(1,50)
adivina = int(input("Adivina numero entre 1 y 50: "))

while adivina != numero:
    if adivina < numero:
        print("El numero es mayor que este. INTENTA DE NUEVO!")
        adivina = int(input("\nAdivina un numero entre 1 y 50: "))
    else:
        print("El numero es menor que este. INTENTA DE NUEVO!")
        adivina = int(input("\nAdivina un numero entre 1 y 50: "))

print("Adivinaste el numero correctamente!")