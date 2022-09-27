def notaDefinitiva(notaFinal):
    valoracionFinal='Desconocida'
    if notaFinal>=3.0 and notaFinal<=5.0:
        valoracionFinal='Ha aprobado el curso'
    elif notaFinal<=2.99 and notaFinal>=2.0:
        valoracionFinal='Puede habilitar el curso'    
    elif notaFinal>=5.1:
        valoracionFinal='No hay calificacion por encima de 5'
    else:
        valoracionFinal='No puede recuperar la materia contacte con el tutor '
    return valoracionFinal
notasDefinitivas=float(input('Ingrese la nota del alumno: '))
print(notaDefinitiva(notasDefinitivas))