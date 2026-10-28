import unittest
from app import add

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_zero_identity(self):
        self.assertEqual(add(0, 7), 7)

if __name__ == "__main__":
    unittest.main()
