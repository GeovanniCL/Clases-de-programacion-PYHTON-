# lista - arreglo
# una Lista se puede iterar :_que se puede repetir el proceso si mismo 

lista = [1, 2, 3, 4, 5, 6.5, 7, "ocho", 9,]
# Puede conter varios tipos de datos 
# Puede repetirse los datos 
print(lista)

# la forma mas facil de usar la lista 
""""
for cada_elemto in lista :
    print(cada_elemto) #imprime cada elemento de nuna lista 
"""

#añadir un elemnto ala lista al final de esta 
print("---------append-------------")
lista.append(10)
print (lista)

#Extiende la lista con otra lista al final
print("---------extend-------------")
lista2 = [0, True, False]
print(lista)
print(lista2)
lista.extend(lista2) #Sumar una lista con un + suma una lista print(lista + lista2)
print(lista)

#Insertar un elemento ala lista en cualquier lugar 
print("---------insert-------------")
lista.insert(2, 2.5)#se puede extender tambien con otra lista 
print(lista) # el primer valor es el lugar y el segundo el dato que e dese ingresar

#busca en orden de izquierda a derecha un elemento con ese valor para quitarlo  
print("---------remove -------------")
print(lista)
lista.remove(2.5)
print(lista)

#elimina un elemento en el espacio seleccionado
print("---------POP-------------")
print (lista.pop(-1,))
print(lista)
print (lista.pop(-1,))
print(lista)

#busca y devuelve un el iniddice/espacio que se igual al elejido
print("---------index-------------")
print(lista.index("ocho")) #el primer parametro es para borrarlo 
print(lista) #el inicio  el final del la busqueda 
print(lista.index(0, 1, 11))
print(lista)

#hacer una copia de  una lista
        #EXISTE 2 TIPOS DE COPIAS LA SUPERFICIL LA PROFUNDA 
"""
1lista = [1,2,3] 
2lista = 1lista #esto es un apuntantador y no una copia como tal de la lista
"""
#esta es una copia superficial de la lista 1
lista_copia = lista.copy()
print(lista_copia)

#contar cuantos elementos hay en la lista 
print("---------Count-------------")
print (lista.count(1))

#ordenar una lisrta 
lista.remove("ocho")
print(lista)
lista.sort() #puede ordenar numeros con numeros letras con letras, pero no puede ordenar palabras y numeros
print(lista)

#revertir una lista 
print("---------revert-------------")
print(lista)
lista.reverse()
print(lista)
#Elimina lso elementos de un lista, pero sigue existeiendo la lista
print("---------Clear-------------")
lista.clear()
print(lista)

#DEll alimiana los elemntos y la lista 
del lista