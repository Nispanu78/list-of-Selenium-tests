import unittest

class TestAssertListEqual(unittest.TestCase):
    def test_list_equal(self):
        list1 = ['python', 'selenium', 'apress']
        list2 = ['python', 'selenium', 'Fernando']

        self.assertListEqual(list1, list2, "Lists do not match")

if __name__ == '__main__':
    unittest.main()