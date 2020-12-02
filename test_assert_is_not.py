import unittest

class TestAssertIsNot(unittest.TestCase):
    def test_assert_is_not(self):
        language="Python"
        self.assertIsNot(language, "Python", "Value is a Match")

if __name__ == '__main__':
    unittest.main()