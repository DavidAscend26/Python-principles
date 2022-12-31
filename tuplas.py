#Caso de uso de las tuplas.
#No se pueden modificar los elementos de una tupla...
frutas = ('Naranja', 'Jicama', 'Guayaba')

print(type(frutas))
for fruta in frutas:
    print(fruta)

#...a menos que se convierta la tupla a una lista, se hagan los cambios necesarios...
frutasLista = list(frutas)
frutasLista[0] = "Pera"
#...y se convierta la lista a tupla nuevamente
frutas = tuple(frutasLista)
print(frutas)


