import unittest

from mathOp import factorial

class ErrorsTestCase(unittest.TestCase):

    def test_factorial_5(self):
        factorial_5 = factorial(5)
        self.assertTrue(factorial_5 == 120)

    
if __name__ == '__main__':
    unittest.main()
