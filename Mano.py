from Baraja import Baraja

class Mano:

    # Atributos
    mano = []

    # Constructor
    def __init__(self, mazo:Baraja):        
        self.mano = [mazo.get_carta() for i in range(0,5)]        

    # Imprime la mano del jugador
    def despliega(self):
        print("------------")
        for x in self.mano:
            x.despliega()        
    
    def puntuar_mano(self):
        self.diccionario_cartas = {}
        for carta in self.mano:
            if carta.letra in self.diccionario_cartas:
                self.diccionario_cartas[carta.letra] += 1
            else:
                self.diccionario_cartas[carta.letra] = 1        
        print(self.diccionario_cartas)
        

if __name__ == "__main__":
    baraja = Baraja()
    j1 = Mano(baraja)
    j2 = Mano(baraja)
    
    j1.despliega()
    j1.puntuar_mano()
    
    j2.despliega()
    j2.puntuar_mano()