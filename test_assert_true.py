import unittest

class TestAssertTrue(unittest.TestCase):
    def test_assert_true(self):
        s1="Python"
        s2="Ruby"
        self.assertTrue(s1==s2, "It's not a Match")

if __name__ == '__main__':
    unittest.main()