from Baraja import Baraja
from Mano import Mano

def main():
    baraja = Baraja()

    # Jugador1    
    jugador1 = Mano(baraja)
    jugador1.despliega()
    jugador1.puntuar_mano()
    print(jugador1)

    # Computadora    
    cpu = Mano(baraja)
    cpu.despliega()
    cpu.puntuar_mano()
    print(cpu)

    if jugador1.puntos > cpu.puntos:
        print(f"\nGano jugador1 {jugador1.puntos} a {cpu.puntos}")
    else:
        if jugador1.puntos < cpu.puntos:
            print(f"\nGano la computadora {cpu.puntos} a {jugador1.puntos}")
        else:
            print(f"\nEmpate")

if __name__ == '__main__':
    main()