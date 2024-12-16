#juego de tribia - este si más o menos tengo una idea 
# juego debe tener varias preguntas, cada una con varias opciones de respuesta.
#El jugador podrá elegir una de las opciones.
#El programa debe indicar si la respuesta es correcta o incorrecta, y mantener el puntaje.
#Al final del juego, el programa debe mostrar el puntaje total.
#El jugador puede intentar una vez por pregunta.

import re
import random
import os
import time

#decoracion 
bienvenida = ("____________¡Bienvenido al Juego de Trivia!____________\n")
personalizacion = ("___________PERSONALIZA TU EXPERIENCIA________________ ")

#funcion para limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

preguntas = {
    "facil" : [
        {"¿Cuál es el color del cielo en un día despejado?\nA)Azul!\nB)Verde\nC)Rojo\nD)Amarillo" : "a"},
        {"¿Cuántos días tiene una semana?\nA)5\nB)7!\nC)6\nD)8" : "b"},
        {"¿En qué continente se encuentra Egipto?\nA)Asia\nB)Europa\nC)África!\nD)Oceanía" : "c"},
        {"¿Cual es la raíz cuadrada de 11?\nA)121\nB)212\nC)120\nD)111" : "d"},
        {"¿Qué animal es conocido por ser el mejor amigo del hombre?\nA)Gato\nB)Perro!\nC)Conejo\nD)Elefante" : "b"}
    ],
    "medio" : [
        {"¿Qué país tiene más habitantes del mundo?\nA)India\nB)Estados Unidos\nC)China!\nD)Rusia" : "c"},
        {"¿Cuántos planetas hay en el sistema solar?\nA)7\nB)9\nC)8!\nD)10" : "c"},
        {"¿Qué metal es conocido por su símbolo 'Au'?\nA)Plata\nB)Oro!\nC)Hierro\nD)Cobre" : "b"},
        {"¿Cuál es la capital de Francia?\nA)Madrid\nB)Roma\nC)París!\nD)Berlín" : "c"},
        {"¿Quién pintó la Mona Lisa?\nA)Picasso\nB)Dalí\nC)Van Gogh\nD)Da Vinci!" : "d"}
    ],
    "dificil" : [
        {"¿Qué filósofo escribió 'La República'?\nA)Aristóteles\nB)Platón!\nC)Sócrates\nD)Nietzsche" : "b"},
        {"¿En qué año se cayó el Muro de Berlín?\nA)1985\nB)1989!\nC)1991\nD)1993" : "b"},
        {"¿Cómo se llama el proceso por el cual las plantas convierten la luz en energía?\nA)Respiración\nB)Fermentación\nC)Fotosíntesis!\nD)Metabolismo" : "c"},
        {"¿Quién descubrió la teoría de la relatividad?\nA)Newton\nB)Einstein!\nC)Tesla\nD)Curie" : "b"},
        {"¿Cuál es el elemento químico con el símbolo 'W'?\nA)Wolframio!\nB)Tungsteno\nC)Magnesio\nD)Cobalto" : "a"}
    ]
}


#el inicio de la clase 
class trivia:
    #atributos - constructor de la clase 
    def __init__(self, dificultad):
        self.dificultad = dificultad
        self.puntaje = {"aciertos": 0, "fallos" : 0 } 
        self.estado = True

    #contuctor de la clase
    def contar_puntaje(self): #para el puntaje del juego 
        self.puntaje["aciertos"] += 1

    #la mecanica del juego 
    def dificultad(nivel):
        if isinstance(nivel, str): 
            pregunta_aleatoria = random.choice(preguntas[nivel])
            pregunta_aleatoria
            for pregunta, llave in pregunta_aleatoria.items():
                respuesta = input(f"{pregunta}\n ¿cúal escoges?: ").lower().strip
                respuesta_limpia = re.sub(r"[()]", "", respuesta)
                inicio = True
                while inicio:
                    if respuesta is not "a" or respuesta is not "b" or respuesta is not "c" or respuesta is not "d":
                        print ("Escoge una opcion indicada en letra que este en pantlla")
                    elif respuesta_limpia == llave :
                        print("Bien echo es la correcta, sigue haci \n+1 punto ")
                        time.sleep(3)
                        limpiar_pantalla()
                        inicio = False
                    else:
                        print("Tan cerca, buena suerte para la siguiente")
                        time.sleep(3)
                        limpiar_pantalla
                        inicio=False
        elif isinstance(nivel, list):
            pass
    
    #define si la perosna gano o perdio 
    def estado_juego(self):
        pass

limpiar_pantalla() #limpia par quitar todo lo anterior

#incio del juego 
while True: 
    bucle = True #bucle de selecion de nivel
    while bucle:
        print(bienvenida)
        print("Responde correctamente las preguntas para ganar puntos.\n")
        nivel = int(input("Elige el nivel que deseas jugar: \n1.-Nivel facil, \n2.-Nivel medio, \n3.-Nivel dificil \n4.-Personalizado \n ¿Cúal eliges?:  "))
        if nivel <= 3:
            print("Ok")
            bucle = False
            time.sleep(2)
            limpiar_pantalla()
        elif nivel == 4: #personalizar el nivel aqui deberia ser xcuantas preguntas en tortla y haci 
            print("Ok")
            bucle = False
            time.sleep(1)
            limpiar_pantalla()

            eleccion = True
            while eleccion:
                print(bienvenida)
                print("Escoge cuantas preguntas quieres por cada dificualtad \n maximo 5 por cada nivel ")
                facil = int(input("Cuantas preguntas Nivel  facil  :"))
                medio = int(input("Cuantas preguntas Nivel  Medio  :"))
                dificil = int(input("Cuantas preguntas Nivel Dificil :"))
                if facil > 5 or medio > 5 or dificil > 5:
                    print("El nivel es mayor a 5  ")
                    time.sleep(2)
                    limpiar_pantalla()
                else:
                    eleccion = False
                    time.sleep(2)
                    nivel = [facil, medio, dificil]
                    limpiar_pantalla()
            #aqui sale del bucle 
        else:
            print("Escoge uno que este en el rango ")
            time.sleep(2)
            limpiar_pantalla()

        #juego 
        cantidad = len(preguntas[nivel]) # lo que hace es que si agrego nuevas preguntas nose rompa el juego 
        juego = trivia(nivel) #juego, solo si nivel esta en el rango de lo contrario n

    # for i in range(cantidad): #cantidad me permite poner mas preguntas sin que tenga que modificar mucho el código 