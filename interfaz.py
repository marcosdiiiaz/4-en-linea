from cuatroenlinea import CuatroEnLinea
import os


class Interface():

    def juego(self):
        self.cuantroenlinea = CuatroEnLinea()
        while True:
            os.system("cls")
            print("## Cuatro en Linea ##\n")
            self.mostrarTablero()
            self.obtenerJugador()
            self.analizar()

    def mostrarTablero(self):
        tablero = ""
        for fila in self.cuantroenlinea.tablero:
            for indice, columna in enumerate(fila):
                tablero += str(columna) + " - "
                if indice == 7:
                    tablero = tablero[:-3]
                    tablero += "\n"
        print(tablero)

    def comprobarNumero(self, columna):
        return False if(columna > 0 and columna < 9) else True

    def analizar(self):
        ganador = self.cuantroenlinea.analizar()
        if ganador > 0 and ganador < 3:
            os.system("cls")
            self.mostrarTablero()
            print(f"Gano el jugador {ganador}")
            exit()
        
        if ganador == 3:
            os.system("cls")
            print("## Cuatro en Linea ##\n")
            self.mostrarTablero()
            print("EMPATE!")
            exit()

    def obtenerJugador(self):
        self.turno = self.cuantroenlinea.definir_turnos()
        flag = True
        while flag:
            columna = int(
                input(f"Turno del jugador {self.turno}!\nElija una columna (1-8): "))
            flag = self.comprobarNumero(columna)
            if flag:
                os.system("cls")
                print("## Cuatro en Linea ##\n")
                self.mostrarTablero()
                print("Ingrese un numero entre el 1 y el 8")
        self.cuantroenlinea.calcular_posicion(columna-1)

    def inicio(self):
        self.juego()