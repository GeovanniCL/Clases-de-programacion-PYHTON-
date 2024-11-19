lista =[1,2,3,4,3,2,1,4,5,5,6,6,7,8,7,8,9,10,11]
lista2 = []
print(lista)


for numero in lista:
    if numero not in  lista2:
        lista2.append(numero)
print(lista2)
