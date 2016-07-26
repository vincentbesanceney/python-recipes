from itertools import tee


def partition(iterable, condition=bool):
    '''Split a sequence in two, based on a predicate.

    Returns two generators, the first one returning elements from the sequence
    which predicate is True, the second one returning elements which predicate
    is False.
    '''
    assert callable(condition), 'Expected callable, got {!r}'.format(condition)

    # Original implementation from Peter Otten: tee gets a generator expression
    # that produces the original elements along with the result of calling the
    # predicate. That is tee'd into two iterables, which are then fed to two
    # generator expressions to select the proper values.
    l1, l2 = tee((condition(elem), elem) for elem in iterable)
    return ((elem for pred, elem in l1 if pred),
            (elem for pred, elem in l2 if not pred))


def uniquify(iterable):
    '''Remove duplicates from a sequence.

    Note: the items from the sequence shall be hashable.
    '''
    seen = set()
    for i in iterable:
        if i not in seen:
            seen.add(i)
            yield i
