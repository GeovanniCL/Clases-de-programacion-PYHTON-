#list compresion 
#Es una manera consisa de crear una lista 


#1era forma
cuadrados = []
for numeros in range(10 + 1):
    cuadrados.append(numeros **2)
print(cuadrados)

#2da forma 
cuadrados2 = list(map(lambda numero: numero **2, range(10 + 1) ))
print(cuadrados2)

#3ra forma 

cuadrados3 = [numero ** 2 for numero in range(10 + 1)]
print(cuadrados3)

#4ta forma 
from math import pi
print( [round(pi , i ) for  i in range (1,6)])

print ("---------------------------")

pares = [numero for numero in range(1, 18) if numero % 2 == 0]
print(pares)
