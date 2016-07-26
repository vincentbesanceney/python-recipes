import logging

from time import time


def singleton(cls):
    '''Decorator that restricts the instantiation of a class to one object.

    This decorator implements the singleton pattern. This is useful when exactly
    one object is needed to coordinate actions across the system.

    Usage:

        >>> @singleton
        ... class My(object):
        ...     pass
        >>> My() == My
        True

    '''
    instance = cls()
    instance.__class__.__call__ = lambda cls: cls
    return instance


def benchmark(func):
    '''Decorator that outputs the execution time of a function.

    Usage:

        >>> from math import sqrt
        >>> @benchmark
        ... def fibo(n):
        ...     return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
        >>> fibo(10)

    '''
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        logging.debug('%r ran in %s secs', func.__name__, time()-start_time)
        return res
    return wrapper
