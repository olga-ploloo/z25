import unittest
from homework import Fibonacci, Even, Factorial


class HomeworkTest(unittest.TestCase):

    def test_Fibonacci(self):
        obj = list(Fibonacci(15))
        self.assertEqual(obj, [0, 1, 1, 2, 3, 5, 8, 13])
        obj = list(Fibonacci(21))
        self.assertEqual(obj, [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_Even(self):
        obj = list(Even(10))
        self.assertEqual(obj, [0, 2, 4, 6, 8, 10])
        obj = list(Even(17))
        self.assertEqual(obj, [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_Factorial(self):
        obj = list(Factorial(5))
        self.assertEqual(obj, [1, 2, 6, 24, 120])
        obj = list(Factorial(10))
        self.assertEqual(obj, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800])


if __name__ == '__main__':
    unittest.main()

