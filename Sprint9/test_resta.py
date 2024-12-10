import unittest
from resta import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 3), -3)
        self.assertEqual(restar(-1, -1), 0)

if __name__ == "__main__":
    unittest.main()