from Carta import Carta

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

    def despliega(self):
        for carta in self.lista_cartas:
            carta.despliega()

if __name__ == "__main__":
    baraja = Baraja()
    baraja.despliega()