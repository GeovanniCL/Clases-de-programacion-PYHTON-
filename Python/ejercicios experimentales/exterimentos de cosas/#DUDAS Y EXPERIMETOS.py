#DUDAS Y EXPERIMETOS 

import time 
import random
import re
import os


#decoracion 
bienvenida = ("____________¡Bienvenido al Juego de Trivia!____________\n")
personalizacion = ("____________PERSONALIZA TU EXPERIENCIA________________ ")

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

"""class trivia:
    #atributos - constructor de la clase 
    def __init__(self, dificultad):
        self.dificultad = dificultad
        self.puntaje = {"aciertos": 0, "fallos" : 0 } 
        self.estado = True

    def conprobador(self, ):
        if isinstance(self.dificultad, str):
            self.niveles()
        elif isinstance(self.dificultad, list):
            self.personalizado()

    def puntaje():
        pass

    def niveles(self):
            pregunta_aleatoria = random.choice(preguntas[nivel])
            for pregunta, llave in pregunta_aleatoria.items():
                respuesta = input(f"{pregunta}\n ¿cúal escoges?: ").lower().strip
                respuesta_limpia = re.sub(r"[()]", "", respuesta)
                inicio = True
                while inicio:
                    if respuesta is not "a" or respuesta is not "b" or respuesta is not "c" or respuesta is not "d":
                        print ("Escoge una opcion indicada en letra que este en pantlla")
                    elif respuesta_limpia == llave :
                        print("Bien echo es la respuesta correcta, sigue haci \n+1 punto ")
                        time.sleep(3)
                        inicio = False
                    else:
                        print("Tan cerca, buena suerte para la siguiente")
                        time.sleep(3)
                        inicio=False

    def personalizado():
        pass

    def estado_juego():
        if cantidad > 0:
            return
        return cantidad > 0

nivel = input("ingrese un nivel: ")


juego = trivia(nivel)
cantidad = len(nivel)
"""


cantidad = 5

lista = [1,2,3,4 ,5 ,6, 7, 8, 9, 10 ]



for i in range(cantidad):
    print(lista)
    numero = random.choice(lista)
    lista.remove(numero)
    