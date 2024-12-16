import random
import os
import time

# El bus
bus1 = " _____________"
bus2 = " |            |"
bus3 = " | ▢ ▢ ▢ ▢  |____"
bus4 = " |___________▯____|"
bus5 = "    ◯          ◯ \n "

# Función de limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Bus:
    def __init__(self, nombre, velocidad, limite_pantalla):
        self.nombre = nombre
        self.posicion = 0
        self.velocidad = velocidad
        self.limite_pantalla = limite_pantalla  # Límite máximo de movimiento

    def mover(self):#0          # 1
        if self.posicion + self.velocidad < self.limite_pantalla:  # No exceder el límite
            self.posicion += self.velocidad

    def dibujar(self):
                            #0
        espacio = " " * self.posicion
        return f"{espacio}{self.nombre}\n{espacio}{bus1}\n{espacio}{bus2}\n{espacio}{bus3}\n{espacio}{bus4}\n{espacio}{bus5}"

# Crear varios autobuses con diferentes velocidades
num_buses = 3
limite_pantalla = 70
buses = [
    Bus(f"Bus {i + 1}", random.randint(1, 3), limite_pantalla)
    for i in range(num_buses)
]
"""
    buses [nose por el momento ]

    class bus:
        BUS = I
    
    for in rage (num_buses)
"""

# Bucle principal del juego
while True:
    limpiar_pantalla()
    
    # Dibujar todos los autobuses
    for bus in buses:
        print(bus.dibujar())
        bus.mover()
    
    time.sleep(0.2)
