#Uso de set. Y diferencias con una lista o una tupla.
#No mantiene un orden, no se pueden modificar los valores y tampoco se pueden duplicar valores. Pero sí podemos agregar o eliminar elementos
planetas = {'Marte', 'Saturno', 'Neptuno', 'Plutón'}
print(planetas)
print('Marte' in planetas)
planetas.add('Tierra')
print(planetas)
#No acepta elementos duplicados
planetas.add('Tierra')
planetas.add('Tierra')
planetas.add('Tierra')
print(planetas)
#Eliminar un elemento sin arrojar error
planetas.discard('Plutón')
planetas.remove('Tierra')
print(planetas)
#Limpiar set
planetas.clear()
#Eliminar el set
del planetas

