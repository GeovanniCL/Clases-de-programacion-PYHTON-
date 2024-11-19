#librerias 
import random
import os 
import time 

#el bus
nombre = ""
bus1 = " _____________"
bus2 = " |            |"
bus3 = " | ▢ ▢ ▢ ▢  |____"
bus4 = " |___________▯____|"
bus5 = "    ◯          ◯ \n "

#funcion de limpiar pantalla

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class buses:
    #constructor 
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.posicion = 0 
        self.velocida = velocidad

    #funcion
    def movimiento_bus(self):
        for i in range(70):
            print(" " * (i + 0) +  self.nombre)
            print(" " * (i + 0) +  bus1)
            print(" " * (i + 0) +  bus2)
            print(" " * (i + 0) +  bus3)
            print(" " * (i + 0) +  bus4)
            print(" " * (i + 0) +  bus5)
            time.sleep(random.uniform(0.03 , 0.3))
            limpiar_pantalla()

nombre = input("Ingrese un nombre: ")
posicion = (0)

busjugador = buses(nombre)
ga= buses("o")

print(busjugador.movimiento_bus() +  ga.movimiento_bus()) 




