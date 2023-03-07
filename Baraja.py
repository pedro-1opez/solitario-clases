from Carta import Carta
import random

class Baraja:

    # Atributos
    lista_cartas = []

    # Constructor
    def __init__(self):
        simbolos = ["♠","♣","♦","♥","2","3","4","5","6","7","8","9","10"] 
        letras = ["J","Q","K","A"]

        for simbolo in simbolos:
            for letra in letras:
                carta = Carta(simbolo, letra)    
                self.lista_cartas.append(carta)

    # Imprime la baraja
    def despliega(self):
        for carta in self.lista_cartas:
            carta.despliega()
    
    # Obtiene una carta de la baraja
    def get_carta(self):        
        index = random.randint(0, len(self.lista_cartas) - 1) # Generamos el indice de la carta a escoger
        return self.lista_cartas.pop(index) # Removemos una carta por medio del indice y regresamos la carta

if __name__ == "__main__":
    baraja = Baraja()    
    carta = baraja.get_carta()    
    carta.despliega()
        
    baraja.despliega()