import unittest

class TestAssertTupleEqual(unittest.TestCase):
    def test_tuple_equal(self):
        tuple1 = ('python', 'selenium', 'apress')
        tuple2 = ('python', 'selenium', 'Fernando')

        self.assertTupleEqual(tuple1, tuple2, "Tuples do not match")

if __name__ == '__main__':
    unittest.main()