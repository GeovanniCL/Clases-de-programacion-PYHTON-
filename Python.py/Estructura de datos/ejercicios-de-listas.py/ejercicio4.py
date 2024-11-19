"""
Dada una lista de números, necesitas separar los números en dos categorías:
pares e impares. Luego, calcula la suma de cada categoría y muestra cuál 
de las dos es mayor. Si ambas sumas son iguales, indícalo.
"""

lista_numeros = [2,3,4,5,10,12,34,71,906,8,9,23,34]
numeros_pares = []
numeros_impares = []

for i in lista_numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

if sum(numeros_impares) > sum(numeros_pares):
    print("La suma de los números impares es mayor que la de los pares.")
elif sum(numeros_impares) < sum(numeros_pares):
    print("La suma de los números pares es mayor que la de los impares.")
else:
    print("Las sumas de los números pares e impares son iguales.")