import unittest
from division import dividir

class TestDivision(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertAlmostEqual(dividir(5, 2), 2.5)
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == "__main__":
    unittest.main()