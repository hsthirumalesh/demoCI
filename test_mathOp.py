import unittest

from mathOp import factorial

class ErrorsTestCase(unittest.TestCase):

    def test_factorial_4(self):
        factorial_4 = factorial(4)
        self.assertTrue(factorial_4 == 24)    
    
    def test_factorial_5(self):
        factorial_5 = factorial(5)
        self.assertTrue(factorial_5 == 120)

    
if __name__ == '__main__':
    unittest.main()
