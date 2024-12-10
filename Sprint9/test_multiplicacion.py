import unittest
from multiplicacion import multiplicar

class TestMultiplicacion(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(0, 3), 0)
        self.assertEqual(multiplicar(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()