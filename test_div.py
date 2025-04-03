import unittest
from main import div

class TestDivisionFunction(unittest.TestCase):

    def test_positive_numbers(self):
        result = div(10, 2)
        self.assertEqual(result, 5.0)

    def test_negative_numbers(self):
        result = div(-10, -2)
        self.assertEqual(result, 5.0)

    def test_mixed_sign_numbers(self):
        result = div(-10, 2)
        self.assertEqual(result, -5.0)

    def test_divide_by_one(self):
        result = div(10, 1)
        self.assertEqual(result, 10.0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

if __name__ == "__main__":
    unittest.main()
