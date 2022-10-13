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
        self.assertEqual(objeto.turno, 2)
        objeto.definir_turnos()
        self.assertEqual(objeto.turno, 1)

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
        self.assertEqual(objeto.ganador(), 'ganaste')

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
        self.assertEqual(objeto.ganador(), 'ganaste')


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
        self.assertEqual(objeto.ganador(), 'ganaste')

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
        self.assertEqual(objeto.ganador(), 'ganaste')

if __name__ == '__main__':
    unittest.main()