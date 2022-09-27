import random
def NumeroAleatorio(numero):
    aleatorio = random.randint(1, 100)
    intentos = 1
    while numero!= aleatorio:
        if (numero < aleatorio):
            print('El número es mayor\U0001F606')
        elif (numero > aleatorio):
            print('El numero es menor\U0001F606 ')
        numero = (int(input('Ingrese nuevamente el numero : ')))
        intentos = intentos+1
    return 'Correcto el número es -> '+str(aleatorio) +', has consumido un total de: '+str(intentos)+ ' intentos.'
    
numeroCalculo=(int(input('Ingrese el número entre 1 y 100: ')))
print(NumeroAleatorio(numeroCalculo))