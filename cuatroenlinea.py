class CuatroEnLinea():

    def __init__(self):
        self.tablero = [[0 for columna in range(8)] for fila in range(8)]
        self.turno = 2
        
    def definir_turnos(self):
        if self.turno == 2:
            self.turno = 1
        else:
            self.turno = 2
        return self.turno

    def calcular_posicion(self, columna):
        for fila in range(7, -1, -1):
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = self.turno
                return self.tablero

    def analizar(self):
        if self.ganador_horizontal() != 0:
            return self.ganador_horizontal()
        if self.ganador_vertical() != 0:
            return self.ganador_vertical()
        if self.ganador_diagonal_derecho() != 0:
            return self.ganador_diagonal_derecho()
        if self.ganador_diagonal_izquierdo():
            return self.ganador_diagonal_izquierdo()
        if self.empate() == 3:
            return self.empate()
        return 0

    def ganador_horizontal(self):
        for fila in range(8):
            for columna in range(8):
                try:
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 1:
                            if self.tablero[fila][columna + 1] == 1:
                                if self.tablero[fila][columna + 2] == 1:
                                    if self.tablero[fila][columna + 3] == 1:
                                        return 1

                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 2:
                            if self.tablero[fila][columna + 1] == 2:
                                if self.tablero[fila][columna + 2] == 2:
                                    if self.tablero[fila][columna + 3] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def ganador_vertical(self):
        for fila in range (8):
            for columna in range(8):
                try:
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 1:
                            if self.tablero[fila + 1][columna] == 1:
                                if self.tablero[fila + 2][columna] == 1:
                                    if self.tablero[fila + 3][columna] == 1:
                                        return 1
                    
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 2:
                            if self.tablero[fila + 1][columna] == 2:
                                if self.tablero[fila + 2][columna] == 2:
                                    if self.tablero[fila + 3][columna] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def ganador_diagonal_derecho(self):
        for fila in range (8):
            for columna in range(8):
                try:
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 1:
                            if self.tablero[fila + 1][columna + 1] == 1:
                                if self.tablero[fila + 2][columna +2] == 1:
                                    if self.tablero[fila + 3][columna + 3] == 1:
                                        return 1
                    
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 2:
                            if self.tablero[fila + 1][columna + 1] == 2:
                                if self.tablero[fila + 2][columna +2] == 2:
                                    if self.tablero[fila + 3][columna + 3] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def ganador_diagonal_izquierdo(self):
        for fila in range (8):
            for columna in range(7, -1, -1):
                try:
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 1:
                            if self.tablero[fila + 1][columna - 1] == 1:
                                if self.tablero[fila + 2][columna - 2] == 1:
                                    if self.tablero[fila + 3][columna - 3] == 1:
                                        return 1
                    
                    if self.tablero[fila][columna] != 0:
                        if self.tablero[fila][columna] == 2:
                            if self.tablero[fila + 1][columna - 1] == 2:
                                if self.tablero[fila + 2][columna - 2] == 2:
                                    if self.tablero[fila + 3][columna - 3] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def empate(self):
        count = 0
        for row in self.tablero:
            count += row.count(0)
        return 3 if count < 1 else 0