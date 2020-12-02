import unittest

class TestAssertSetEqual(unittest.TestCase):
    def test_set_equal(self):
        set1 = {'python', 'selenium', 'apress'}
        set2 = {'python', 'selenium', 'Fernando'}

        self.assertSetEqual(set1, set2, "Sets do not match")

if __name__ == '__main__':
    unittest.main()