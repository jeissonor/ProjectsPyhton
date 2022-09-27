'''monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa  \U0001F910: ")
print(monedas.get(moneda.title(), "La divisa no está."))'''


'''miDiccionario={'Colombia':'Bogota','España':'Madrid','Ecuador':'Quito'}
miPais=input('ingrese el pais a consultar en el diccionario: ')
print(miDiccionario.get(miPais.title(),'El país no esta disponible \U0001F910'))'''




nombre=input('Ingrese el nombre completo: ')
edad= int(input('Ingrese la edad: '))
direccion=input('Ingrese la direccion: ')
telefono=int(input('Ingrese su número de contacto: '))
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])


