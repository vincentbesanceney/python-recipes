import unittest

from iterables import partition
from iterables import uniquify


class IterablesTests(unittest.TestCase):

    def test_partition(self):
        def is_odd(i):
            return bool(i % 2)
        expected_odds = range(1, 10, 2)
        expected_evens = range(0, 10, 2)
        actual_odds, actual_evens = partition(range(10), is_odd)
        self.assertEqual(list(expected_odds), list(actual_odds))
        self.assertEqual(list(expected_evens), list(actual_evens))


    def test_uniquify(self):
        elems = ['a', 'b', 'c', 'a', 'd', 'b', 'e']
        expected = ['a', 'b', 'c', 'd', 'e']
        actual = list(uniquify(elems))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
