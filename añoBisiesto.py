año=int(input('Ingrese el año a evaluar:'))
def bisiesto(año):
    
    if año%4==0 and año%100!=0:
        print('Es bisiesto')
    elif año%100==0 and año%400==0:
        return ('Es bisiesto')
    else:
        return 'No es bisiesto'      
print(bisiesto(año))