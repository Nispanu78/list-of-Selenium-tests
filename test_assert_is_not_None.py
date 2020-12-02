import unittest

class TestAssertIsNotNone(unittest.TestCase):
    def test_is_not_none(self):
        color=None
        self.assertIsNone(color, "Color is null")

if __name__ == '__main__':
    unittest.main()