from Baraja import Baraja

class Mano:

    # Atributos
    mano = []

    # Constructor
    def __init__(self, mazo:Baraja):        
        self.mano = [mazo.get_carta() for i in range(0,5)]        
        self.dpuntos = {1:1, 2:10, 3:100, 4: 1000}
        self.dmano = {x.letra:x for x in self.mano}
        self.diccionario_cartas = {}
        self.puntos = 0

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
                
        # Puntuar de acuerdo a par, tercia o unico
        self.puntos = 0
        for letra, veces in self.diccionario_cartas.items():
            carta = self.dmano[letra]
            self.puntos += (carta.valor * self.dpuntos[veces])

    def __str__(self):
        return f"{self.diccionario_cartas} Puntos: {self.puntos}"
        

if __name__ == "__main__":
    baraja = Baraja()
    j1 = Mano(baraja)
    j2 = Mano(baraja)
    
    j1.despliega()
    j1.puntuar_mano()
    print(j1)    
    
    j2.despliega()
    j2.puntuar_mano()
    print(j2)