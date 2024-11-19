"""
Escribe un programa que reciba una lista de números, la ordene en orden
ascendente y elimine todos los números pares. Al final, la lista solo
debe contener los números impares en orden ascendente.
"""
lista = [1,5,3,6,8,0,2,4,9,7,10]

lista.sort()
print(lista)

for x in  lista:
    if x % 2 == 0:
        lista.remove(x)

print (lista)