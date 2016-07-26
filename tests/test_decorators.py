import unittest

from decorators import singleton
from decorators import benchmark


class SingletonTests(unittest.TestCase):

    def test_singleton(self):
        @singleton
        class expected(object): pass
        actual = expected()
        self.assertIs(expected, actual)


if __name__ == '__main__':
    unittest.main()
