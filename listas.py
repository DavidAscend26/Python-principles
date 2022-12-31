#Demostración del uso de Listas, acceso a elementos específicos o por rango, agregando, insertando, removiendo elementos, limpiando la lista y eliminando la lista. 
nombres = ['Grandi10', 'Accent', 'Elentra', 'Creta', 'Tucson', 'Santa fe', 'Palisade']

print(nombres[5])
print(nombres[-2])
print(nombres[0:2])
print(nombres[:6])
print(nombres[4:])

nombres.append("Familia Hyundai")

for nombre in nombres:
    print(nombre)

#Agregar un elemento al final de la lista
nombres.append("HB20")
print(nombres)
#Insertar un elemento en un indice especifico
nombres.insert(2, "HB20 SD")
print(nombres)
#Remover el último valor agregado
nombres.pop()
print(nombres)
#Eliminar un elemento por indice
del nombres[4]
print(nombres)
#Limpiar la lista
nombres.clear()
print(nombres)
#Borrar la lista completa
del nombres