import random 
def cuantosIntentosSaldran():
    numeroIntentos=0
    for i in range(3):
        dado=random.randrange(1,10)
        print(f'Tirada {i+1}: {dado}')
        if dado==5:
            numeroIntentos+=1            
    print(f'En total han salido {numeroIntentos} cinco')
    return 'Fin del programa'

print(cuantosIntentosSaldran())