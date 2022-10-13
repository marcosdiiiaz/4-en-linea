class CuatroEnLinea():

    def __init__(self):
        self.tablero = [[0 for columna in range(8)] for fila in range(8)]
        self.jugador1 = 1
        self.jugador2 = 2
        self.turno = self.jugador1
        self.gano = 'ganaste'
        self.empate = 'empataron'

    def definir_turnos(self):
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1
        return self.turno

    def calcular_posicion(self, fila, columna):
        indice = len(self.tablero) - 1  
        while indice >= 0:
            if self.tablero[indice][columna] == 0:
                return indice
            indice -= 1
        return -1

    def ganador(self):
        for fila in range(8):
            for columna in range(8):
                try:
                    if self.tablero[fila][columna] != ' ':
                        if self.tablero[fila][columna + 1]:
                            if self.tablero[fila][columna + 2]:
                                if self.tablero[fila][columna + 3]:
                                    return self.gano
                    return self.empate 

                    if self.tablero[fila][columna] != ' ':
                        if self.tablero[fila + 1][columna]:
                            if self.tablero[fila + 2][columna]:
                                if self.tablero[fila + 3][columna]:
                                    return self.gano
                    return self.empate

                    if self.tablero[fila][columna] != ' ':
                        if self.tablero[fila - 1][columna - 1]:
                            if self.tablero[fila - 2][columna - 2]:
                                if self.tablero[fila - 3][columna - 3]:
                                    return self.gano
                    return self.empate

                    if self.tablero[fila][columna] != ' ':
                        if self.tablero[fila + 1][columna + 1]:
                            if self.tablero[fila + 2][columna +2]:
                                if self.tablero[fila + 3][columna + 3]:
                                    return self.gano
                    return self.empate

                except(Exception):
                    pass

objeto = CuatroEnLinea()

    #def empate(self):
