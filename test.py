import unittest
from cuatroenlinea import CuatroEnLinea

class TestGame(unittest.TestCase):

    def test_crear_tablero(self):
        objeto = CuatroEnLinea()
        self.assertEqual(len(objeto.tablero), 8)
        self.assertEqual(len(objeto.tablero[0]), 8)

    def test_definir_turnos(self):
        objeto = CuatroEnLinea()
        objeto.definir_turnos()
        self.assertEqual(objeto.turno, 1)
        objeto.definir_turnos()
        self.assertEqual(objeto.turno, 2)

    def test_ganador_vertical(self):
        objeto = CuatroEnLinea()
        objeto.tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(objeto.ganador_vertical(), 0)

    def test_ganador_horizontal(self):
        objeto = CuatroEnLinea()
        objeto.tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '2', '2', '2', '2', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(objeto.ganador_horizontal(), 0)

    def test_ganador_diagonal_p1(self):
        objeto = CuatroEnLinea()
        objeto.tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
                           [' ', ' ', ' ', ' ', ' ', ' ', '1', ' '], 
                           [' ', ' ', ' ', ' ', '2', '1', ' ', ' '],
                           [' ', ' ', ' ', ' ', '1', '2', ' ', ' '],
                           [' ', ' ', '2', '1', '2', '2', ' ', ' '],
                           [' ', ' ', '2', '2', '2', '1', ' ', ' '],
                           [' ', '1', '1', '1', '2', '1', ' ', ' '],
                           [' ', '1', '1', '2', '2', '1', ' ', ' ']]
        self.assertEqual(objeto.ganador_diagonal_izquierdo(), 0)

    def test_ganador_diagonal_p2(self):
        objeto = CuatroEnLinea()
        objeto.tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', '2', ' ', ' ', ' ', ' '],
                            [' ', ' ', '2', ' ', ' ', ' ', ' ', ' '],
                            [' ', '2', ' ', ' ', ' ', ' ', ' ', ' '],
                            ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(objeto.ganador_diagonal_derecho(), 0)

    def test_empate(self):
        objeto = CuatroEnLinea()
        objeto.tablero = [['2', '2', '2', '1', '2', '2', '1', '2'], 
                          ['1', '1', '1', '2', '1', '1', '2', '1'], 
                          ['2', '2', '2', '1', '2', '2', '1', '2'], 
                          ['1', '1', '1', '2', '1', '1', '2', '1'], 
                          ['2', '2', '2', '1', '2', '2', '1', '2'], 
                          ['1', '1', '1', '2', '1', '1', '2', '1'], 
                          ['2', '2', '2', '1', '2', '2', '1', '2'], 
                          ['1', '1', '1', '2', '1', '1', '2', '1']]
        self.assertEqual(objeto.analizar(), 3)

    def definir_turnos(self):
        objeto = CuatroEnLinea()
        self.assertEqual(objeto.definir_turnos, 0)
        self.assertEqual(objeto.player_turn(), '1')

if __name__ == '__main__':
    unittest.main()