import unittest

class TestAssertIsNotEqual(unittest.TestCase):
    def test_is_not_equal(self):
        num=7
        num2=8
        self.assertNotEqual(num, num2, "Numbers do match")

if __name__ == '__main__':
    unittest.main()