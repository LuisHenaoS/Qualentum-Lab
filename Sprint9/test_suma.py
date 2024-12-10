import unittest
from suma import sumar

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(0, 0), 0)

if __name__ == "__main__":
    unittest.main()