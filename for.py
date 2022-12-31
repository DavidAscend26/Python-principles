#Demostración del ciclo For, empleando rangos con diferentes características.
cadena = "Hola mundo"

for letra in cadena:
    print(letra)
    if letra == 'o':
        break
else:
    print("Fin ciclo for")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor par: {i}')

for i in range(11):
    if i % 3 == 0:
        print(f'Divisible entre 3: {i}')

for i in range(2,7):
    print(i)

for i in range(3,11,2):
    print(i)