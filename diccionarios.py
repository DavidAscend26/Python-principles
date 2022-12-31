#Uso de los diccionarios y cómo manejarlos.
#Se compone de dos elementos (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario['IDE'])
print(diccionario.get('OOP'))
diccionario['IDE'] = 'modified text'
print(diccionario['IDE'])

for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprobar existencia de algún elemento
print('IDE' in diccionario)

#Agregar un elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)
#Borrar un elmento
diccionario.pop('DBMS')
#Limpiar
diccionario.clear()
print(diccionario)
#Borrar
del diccionario