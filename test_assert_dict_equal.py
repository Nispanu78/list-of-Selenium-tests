import unittest

class TestAssertDictEqual(unittest.TestCase):
    def test_dict_equal(self):
        dict1 = {'lang':'python', 'tool':'selenium', 'publication':'apress'}
        dict2 = {'lang':'python', 'tool':'selenium', 'publication':'Fernando'}

        self.assertDictEqual(dict1, dict2, "Dictionaries do not match")

if __name__ == '__main__':
    unittest.main()