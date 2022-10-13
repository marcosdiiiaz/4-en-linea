from cuatroenlinea import CuatroEnLinea
import os

class Interface():
    
    def juego(self):
        self.cuantroenlinea = CuatroEnLinea()
        while True:
            os.system("cls")
            self.mostrarTablero()
            self.obtenerJugador()
    
    def mostrarTablero(self):
        tablero = ''
        for fila in self.cuantroenlinea.tablero:
            for indice, columna in enumerate(fila):
                tablero += str(columna) + " - "
                if indice == 7:
                    tablero = tablero[:-3]
                    tablero += "\n"
        print(tablero)

    def obtenerJugador(self):
        turno = self.cuantroenlinea.definir_turnos()
        columna = int(input(f"Elija una columna!\nTurno del jugador {turno}:"))
        self.cuantroenlinea.calcular_posicion(columna)
        #posicion = self.cuantroenlinea.
        # llamar a la funcion donde coloca el numero y pasarle como parametro "columna"
        # esa funcion tiene que llevar el numero hasta abajo

    def inicio(self):
        self.juego()
