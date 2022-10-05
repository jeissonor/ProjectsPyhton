import random
def acumaladorFor():
    Acumulador=0
    for i in range(5):
        dado=random.randrange(1,10)
        print(f'Tirada {i+1}:{dado}', end=', ')
        Acumulador+=dado
    return(f'En total se ha obtenido {Acumulador} puntos.')
print(acumaladorFor())