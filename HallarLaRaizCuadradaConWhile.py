import math

print('Programa para  hallar la raíz cuadrada...')
numero=int(input('Introduce un número: '))
intentos =1
while numero<0:
    print('El número no debe ser negativo =(')
    numero=int(input('Ingresa nuevamente el número: '))

    intentos=intentos+1

    if intentos==5:
        break

if intentos ==5:
    print('No puedo hacer el calculo...')

else: 
    print(math.sqrt(numero))

