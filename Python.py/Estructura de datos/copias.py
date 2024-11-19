#esto es una libreria y es una forma de extender pyhon 
import copy

#se puede guardar una lista dentro de otra 
#la primer lista es lista padre, la segunda es hijo, la tecera es nieto 
lista = [1,2,3,[4,5,6,[7]]]
print(lista)

#esta es una lista supeficial
listaCopia = lista.copy()

#esta es  una lista profunda
listaProfunda = copy.deepcopy(lista)


#se puden agregar datos en una lista dentro de una lista 
lista[3].append(9)
lista [3][3].append(8)
#imprimir listas 
print (listaCopia)
print(listaProfunda)