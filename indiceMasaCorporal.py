kilogramosPersona=float(input('Ingrese el peso correcto con decimales: '))
estaturaPersona=float(input('Ingrese la estatura correcta: '))
calculoIndiceMasaCorporal=kilogramosPersona/estaturaPersona**2
print(f'Tu índice de masa corporal es: {calculoIndiceMasaCorporal:.2f} =) ')   