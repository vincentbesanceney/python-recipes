import unittest

from strings import MagicString


class MagicStringTests(unittest.TestCase):

    def test_basic(self):
        expected = 'my_string'
        m = MagicString(expected)
        self.assertEqual(m, expected)
        self.assertEqual(m.origin, expected)

    def test_spell(self):
        expected = 'something completely different'
        class DisclosedString(MagicString):
            spell = lambda x: expected
        m = DisclosedString('secret')
        self.assertEqual(m, expected)
        self.assertEqual(m.origin, 'secret')


if __name__ == '__main__':
    unittest.main()
