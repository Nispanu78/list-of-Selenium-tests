import unittest

class TestAssertGreaterLess(unittest.TestCase):
    def test_is_greater_equal(self):
        num1=7
        num2=8
        self.assertGreaterEqual(num1, num2, str(num1) + " is not greater than " + str(num2))

    def test_is_less_equal(self):
        num3=10
        num4=8
        self.assertLessEqual(num3, num4, str(num3) + " is not less than " + str(num4))

if __name__ == '__main__':
    unittest.main()