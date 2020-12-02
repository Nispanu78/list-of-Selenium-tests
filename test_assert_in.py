import unittest

class TestAssertIn(unittest.TestCase):
    def test_assert_in(self):
        self.collection=set(["Python", "Selenium", "Apress"])
        self.assertIn("Fernando", self.collection, "Element is not available in the set.")
        self.assertNotIn("Java", self.collection, "Element is not available in the set.")
        if __name__ == '__main__':
            unittest.main()

if __name__ == '__main__':
    unittest.main()