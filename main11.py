#iterar un rango de 0 a 10 e imprimir numeross divisibles entre 3
print("Rango de 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

#ejercicio 2 crear un rango de numero de 2 a 6 e imprimelos
print("Rango con valores de inicio ")
rango = range(2,7)
for i in rango:
    print(i)

#crear un rango de 3 a 10 pero con incremento de 2 en 2 en lugar
print("Rango con valores de inicio = 3, fin = 10, incremento = 2")
rango = range(3,11,2)
for i in rango:
    print(i)