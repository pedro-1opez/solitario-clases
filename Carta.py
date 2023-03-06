class Carta:
    
    # Atributos
    simbolo = ""
    letra = ""
    valor = 0
    dvalor = {}        

    # Constructor
    def __init__(self, simbolo, letra):
        self.simbolo = simbolo
        self.letra = letra        
        self.dvalor = self.crea_diccionario()
        self.valor = self.dvalor[self.letra]

    # Metodos internos
    def crea_diccionario(self):
        dvalor = {str(k):k for k in range(2,11)}
        dvalor['J'] = 11
        dvalor['Q'] = 12
        dvalor['K'] = 13
        dvalor['A'] = 14
        
        return dvalor
        
    def despliega(self):        
        print(f"{self.letra} | {self.simbolo} | {self.valor}")

    # Método toString
    def __str__(self):
        print(f"{self.letra}{self.simbolo}")
        

if __name__ == "__main__":
    a = Carta("A","3")
    a.despliega()