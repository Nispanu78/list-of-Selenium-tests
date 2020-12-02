import unittest

class TestAssertIsNone(unittest.TestCase):
    def test_is_none(self):
        color='blue'
        self.assertIsNone(color, "Color is not null")

if __name__ == '__main__':
    unittest.main()