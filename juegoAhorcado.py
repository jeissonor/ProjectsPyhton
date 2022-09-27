import time 
nombre=input('Como te llamas?')
print('Hola,'+ nombre)
print('Hola,'+nombre,'Es hora de jugar al arcohado')
print('')
time.sleep(1)
print('Comience a adivinar')
time.sleep(0.5)
palabra='Jeisson'
tupalabra=''
vidas=5

while vidas>0:
    fallas=0
    for letra  in palabra:
        if letra in tupalabra:
            print(letra,end='')
        else:
            print('*',end='')
            fallas+=1
    if fallas ==0:
        print('')
        print('Felicidades, ganaste')
        break
    tuletra=input('Introduce una letra: ')
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print('Equivocacion')
        print('Tu tienes',vidas,'vidas')
    if vidas==0:
        print('Perdiste!')

else:
    print('Gracias por participar')
