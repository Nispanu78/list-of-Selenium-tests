import unittest

class TestAssertIs(unittest.TestCase):
    def test_assert_is(self):
        language="Python"
        self.assertIs(language, "Selenium", "It's not a Match")

if __name__ == '__main__':
    unittest.main()