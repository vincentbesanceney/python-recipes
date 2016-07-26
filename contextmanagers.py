import sys

from contextlib import contextmanager


@contextmanager
def ignore_exceptions(*exceptions):
    '''Runtime context which ignores given exceptions.

    Usage:

        >>> with ignore_exceptions(AttributeError, ValueError, TypeError):
        ...     i = int(k[v])

    '''
    try:
        yield
    except exceptions:
        pass


@contextmanager
def redirect_stdout(fileobj):
    '''Runtime context which redirects stdout to the given filehandle.

    Usage:

        >>> with open('log.txt', 'w') as fd:
        ...    with redirect_stdout(fd):
        ...        print 'my message'

    '''
    old_stdout, sys.stdout = sys.stdout, fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = old_stdout
