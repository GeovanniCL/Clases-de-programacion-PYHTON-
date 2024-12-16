#segundo proyecto nose ni como haerlo XD
# es un arocado entones necesti
#1 listas,(dividda por categoria)
#2 funcion de crear y dibujar el muñeco
#3 estrucura del juego como tal

import random
import os
import time

#varibles eleciones _______________________________
animales = ["perro", "gato", "elefante", "león", "jirafa", "tigre", "conejo", "oso", "delfín", "canguro"] 
frutas = ["manzana", "banana", "naranja", "fresa", "uva", "mango", "kiwi", "piña", "sandía", "cereza"]
verduras= ["zanahoria", "espinaca", "brócoli", "tomate", "pepino", "lechuga", "papa", "pimiento", "berenjena", "guisante"]

#decoracion_______________________________
decoracion = "==========================EL AHORCADO=================================="

#dibujo -poste
parte1 = "+---+"
parte2 = "|   |"
parte3 = "|"
#dibujo - humano
cabeza = "   O"
brazo1 = "  /" 
cuerpo = "|"
brazo2 = "\ "
pierna1 = "/ " 
pierna2 = "\ "

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#la clase
class ahorcado:
    #construir la clase 
    def __init__(self, palabra):
        self.palabra = palabra
        self. intentos = 6
    
    #dibujar el poste con las varites 
    def dibujo_poste(self):#3
        if self.intentos == 6:  #agrega el poste 
            print(f"{parte1}\n{parte2}\n{parte3}\n{parte3}\n{parte3}\n{parte3}")
        elif self.intentos == 5:#agrega la cabeza
            print(f"{parte1}\n{parte2}\n{parte3}{cabeza}\n{parte3}\n{parte3}\n{parte3}")
        elif self.intentos == 4:#agrega el cuerpo 
            print(f"{parte1}\n{parte2}\n{parte3}{cabeza}\n{parte3}   {cuerpo}\n{parte3}\n{parte3}")
        elif self.intentos == 3:#agrega el brazo derecho 
            print(f"{parte1}\n{parte2}\n{parte3}{cabeza}\n{parte3}{brazo1}{cuerpo}\n{parte3}\n{parte3}")
        elif self.intentos == 2:#agrega el brazo izquierdo
            print(f"{parte1}\n{parte2}\n{parte3}{cabeza}\n{parte3}{brazo1}{cuerpo}{brazo2}\n{parte3}\n{parte3}")
        elif self.intentos == 1:#agrega el pie derecho
            print(f"{parte1}\n{parte2}\n{parte3}{cabeza}\n{parte3}{brazo1}{cuerpo}{brazo2}\n{parte3}  {pierna1}\n{parte3} ")
        elif self.intentos == 0:#agrega el pie izquierdo 
            print(f"{parte1}\n{parte2}\n{parte3}{cabeza}\n{parte3}{brazo1}{cuerpo}{brazo2}\n{parte3}  {pierna1}{pierna2}\n{parte3} ")

    #dibujo de las casillas del juego 
    def dibujo_casilla(self):
        print("". join(casillas))

    #verifica si la letra esta en la palabra y actualiza los intentos 
    def verificar_letra(self, letra_jugador): 
            if letra_jugador in  palabra_random:
                for i, x in enumerate(palabra_random):
                    if x == letra_jugador:
                        casillas[i] = letra_jugador
            else:
                print("letra incorrecta ")
                self.intentos -= 1
                self.estado_juego()
                
    #determian si el juego ya termino 
    def estado_juego(self):
        if self.intentos == 0:
            print ("\nHas perdido 😔🥹 ")
            print(f"la palabra era: {palabra_random}")
        elif self.intentos >= 1:
            print ("\n¡¡ Has ganado 🎊!!")
        

limpiar_pantalla()

estado = True
while estado:
    limpiar_pantalla()
    print(decoracion)
    seleccion = input("¿Deseas jugar? (si/no): ").strip().lower()
    if seleccion == "si":
        limpiar_pantalla()
        #inicio de la categoria 
        categoria = int(input("Ingrese la categoria que deses \n1.-Animales. \n2.-Frutas. \n3.-Verduras.\n "))
        estado2 = True 
        while estado2:
            if categoria == 1:
                palabra_random = random.choice (animales)
                estado2 = False
            elif categoria == 2:
                palabra_random = random.choice (frutas)
                estado2 = False
            elif categoria == 3:
                palabra_random = random.choice (verduras)
                estado2 = False
            else:
                print("Escoge un número o palabra dentro del rango")
        print("\n¡PERFECRTO!")
        time.sleep(2)
        limpiar_pantalla()
        #cofiguracion juego 
        casillas = [" _ "] * len(palabra_random)
        juego = ahorcado(palabra_random)
        #bucle del juego 
        while juego.intentos >= 0:
            print(decoracion)
            juego.dibujo_poste()
            juego.dibujo_casilla()
            if " _ " in casillas and juego.intentos > 0 :
                letra_jugador = input("adivina la letra: ").strip().lower()
                juego.verificar_letra(letra_jugador)
                limpiar_pantalla()
            else:
                juego.estado_juego()
                break
        regreso = input("**Para volver a jugar presiona enter**")
        #si el ususario dice que si 
    elif seleccion == "no":
        print("Ta bien")
        time.sleep(1)
        regreso = input("**Para volver al menu presiona enter**")
        limpiar_pantalla()
        #si el usuario dice que no 
    else:
        print("Elige bien")
        regreso = input("**Para volver al menu presiona enter**")
        time.sleep(1)
        limpiar_pantalla()