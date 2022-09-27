def rentas(rentaIntroducida):
    correspondiente = ''
    if rentaIntroducida < 12000:
        correspondiente = 'Le corresponde el 7%'
    elif rentaIntroducida >= 12000 and rentaIntroducida <= 18000:
        correspondiente = 'Le corresponde el 15%'
    elif rentaIntroducida >= 35000 and rentaIntroducida <= 70000:
        correspondiente = 'Le corresponde el 35%'
    else:
        correspondiente = 'Le corresponde el 45%'
    return correspondiente
 

IngresoRenta = (int(input('Ingrese la renta para verificar su valor de %: ')))
print(rentas(IngresoRenta))
