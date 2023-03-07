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
        

if __name__ == "__main__":
    baraja = Baraja()
    j1 = Mano(baraja)
    j2 = Mano(baraja)
    
    j1.despliega()
    j2.despliega()