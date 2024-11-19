#se basa en el principio el primero que llega es el primero que se va
#FIFO - firts in - firdt out 

#modo facil de hacer una cola 

#esta es una estructrura de datos que implementa una cola en python
#bibioteca mayor      modulo 
from collections import deque

alumnos = deque(["jesus", "Angel", "Guzman"])
print(alumnos)

alumnos.append("Pablo")
alumnos.append("Luis")

print(alumnos)

alumnos.popleft()
print(alumnos)

print("_-------------------------------")


cola = []

cola.append(1)
cola.append(2)
cola.append(3)

print(cola)

cola.pop(0)
print(cola)