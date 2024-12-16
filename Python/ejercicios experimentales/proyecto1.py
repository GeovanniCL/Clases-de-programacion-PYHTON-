import random
import os
import time

# El bus
bus1 = " _____________"
bus2 = " |            |"
bus3 = " | ▢ ▢ ▢ ▢  |____"
bus4 = " |___________▯____|"
bus5 = "    ◯          ◯ \n "

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clase para los buses
class Bus:
    def __init__(self, nombre, velocidad, limite_pantalla):
        self.nombre = nombre
        self.posicion = 0
        self.velocidad = velocidad
        self.limite_pantalla = limite_pantalla
        self.terminado = False

    def cambiar_velocidad(self):
        self.velocidad = random.randint(0,2)  # Cambia la velocidad aleatoriamente

    def mover(self):
        if self.posicion + self.velocidad < self.limite_pantalla:
            self.posicion += self.velocidad
        else:
            self.terminado = True

    def dibujar_bus(self):
        espacio = " " * self.posicion
        return f"{espacio}{self.nombre}\n{espacio}{bus1}\n{espacio}{bus2}\n{espacio}{bus3}\n{espacio}{bus4}\n{espacio}{bus5}"

# Estructura del juego
while True:
    print("Carrera de buses")
    print("________________")
    seleccion = input("¿Deseas jugar? (si/no): ").strip().lower()

    if seleccion == "si":
        limpiar_pantalla()
        cantidad_buses = int(input("Ingrese la cantidad de buses: "))
        nombre_jugador = input("Ingrese un nombre para su bus: ")
        limpiar_pantalla()

        # Contador inicial
        for i in range(3, 0, -1):
            print(f"La carrera inicia en {i}")
            time.sleep(1)
            limpiar_pantalla()

        # Crear los buses
        limite_pantalla = 70
        buses = [
            Bus(f"Bus No {i + 1}", random.randint(1, 3), limite_pantalla)
            for i in range(cantidad_buses)
        ]
        # El primer bus tiene el nombre del jugador
        buses[0].nombre = nombre_jugador

        # Carrera
        while not all(bus.terminado for bus in buses):
            limpiar_pantalla()
            for bus in buses:
                bus.cambiar_velocidad()
                bus.mover()
                print(bus.dibujar_bus())
            time.sleep(0.2)

        # Una vez que la carrera termina, ordenamos por posición final
        buses_ordenados = sorted(buses, key=lambda bus: bus.posicion, reverse=True)

        # Mostrar posiciones finales
        print("¡La carrera ha terminado!")
        for i, bus in enumerate(buses_ordenados):
            # Imprimir el lugar de cada bus
            print(f"{i + 1}° Lugar: {bus.nombre} llegó a la posición {bus.posicion}")
        time.sleep(30)
        #limpiar_pantalla()
    elif seleccion == "no":
        print("Desgraciado, ta bien")
        time.sleep(3)
        limpiar_pantalla()
    else:
        print("Pendejo, elige bien")
        time.sleep(3)
        limpiar_pantalla()
