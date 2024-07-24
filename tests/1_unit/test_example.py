import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    #TODO: def test_subtract(self):

    #TODO def test_multiply(self):

    #TODO def test_divide(self):
    
    #TODO bonus:     def test_divide_raises(self):

if __name__ == '__main__':
    unittest.main()
