from random import randint

numero_aleatorio = randint(1,100)
usuario = input("Tu nombre: ")
intentos = 0
estimado = 0

print(f'Hola {usuario} he pensado un numero aleatorio\n tienes 8 intentos para adivinar')

while intentos < 8:
    estimado = int(input('¿Cual es el numero?: '))
    intentos += 1
    if estimado not in range(1,100):
       print('El numero que has elegido no esta en el rango del 1 al 100')
    if estimado < numero_aleatorio:
       print('El numero es mas alto')
    elif estimado > numero_aleatorio:
       print('El numero es mas bajo')
    else:
       print(f'Felicitaciones {usuario}! has acertado en {intentos} intentos')
       break

if estimado != numero_aleatorio:
    print(f'Has agotado todos los intentos!, en numero secreto era {numero_aleatorio}')










