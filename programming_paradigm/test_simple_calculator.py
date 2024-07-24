import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self): #What does this method does??
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        #self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        #self.assertEqual(self.calc.asubtract(-1, 1), 0)
    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        #self.assertEqual(self.calc.multiply(-1, 1), 0)
    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(12, 3), 4)
        #self.assertEqual(self.calc.divide(-1, 1), 0)
        #self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)