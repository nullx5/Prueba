 
#Este es el juego adivina el numero.

import random

intentosRealizados = 1

print("                  ### ADIVINA EL NUMERO ###")

print("!Hola¡ ¿Como te llamas?")
miNombre = input()

numero = random.randint(1, 20)
print("Bueno," + miNombre + ",estoy pensando en un numero entre 1 y 20.")

while intentosRealizados < 6:
    print("Intenta adivinar")
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print("Tu estimacion es muy baja")

    if estimacion > numero:
        print("Tu estimacion es muy alta")

    if estimacion == numero:
        break
    
    
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print("¡Buen trabajo, " + miNombre + " ,Has adivinado mi numero en" + intentosRealizados + "intentos")

if estimacion != numero: 
    numero = str(numero)
    print("Pues NO, el numero que estaba pensando era  " + numero)
