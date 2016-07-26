import unittest

from contextmanagers import ignore_exceptions
from contextmanagers import redirect_stdout

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


class IgnoreExceptionTests(unittest.TestCase):

    def test_no_error(self):
        expected = 1
        with ignore_exceptions(TypeError):
            actual = int('1')
        self.assertEqual(expected, actual)

    def test_ignore_type_error(self):
        expected = None
        with ignore_exceptions(TypeError):
            expected = int(None)
        self.assertIsNone(expected)

    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            with ignore_exceptions(AttributeError, ValueError):
                int(None)


class RedirectStdout(unittest.TestCase):

    def test_redirect_print(self):
        fileobj = StringIO()
        expected = 'my message'
        with redirect_stdout(fileobj):
            print(expected)
        actual = fileobj.getvalue().strip()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
