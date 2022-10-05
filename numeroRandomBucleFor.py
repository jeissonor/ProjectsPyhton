import random
def numeroRandom():
    numeroCinco=False
    for i in range(3):
        dado=random.randrange(1,10)
        print(f'Tirada número {i+1} = {dado}')
        if dado==5:
            numeroCinco=True
    if numeroCinco:
        print('Ha sacado por lo menos un Cinco =)')
    else:
        print('Debe seguir intentando =(')
    return 'Fin del programa'
print(numeroRandom())        

