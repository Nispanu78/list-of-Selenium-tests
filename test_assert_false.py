import unittest

class TestAssertFalse(unittest.TestCase):
    def test_assert_false(self):
        s1="Python"
        s2="Ruby"
        self.assertFalse(s1==s2, "It's a Match")

if __name__ == '__main__':
    unittest.main()