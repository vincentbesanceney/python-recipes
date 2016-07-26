'''Run unit tests.

Usage:

    python runtests.py [flags] ...

For full help, try --help.
'''

from __future__ import print_function

import argparse
import logging
import os
import random
import sys

from random import randrange
from unittest import TextTestRunner
from unittest.loader import defaultTestLoader
from unittest.signals import installHandler


def level(verbosity):
    if verbosity >= 4:
        return logging.DEBUG
    if verbosity == 3:
        return logging.INFO
    if verbosity == 2:
        return logging.WARNING
    if verbosity == 1:
        return logging.ERROR
    return logging.CRITICAL


def directory(arg):
    '''Validate arg is a directory.'''
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        raise argparse.ArgumentTypeError("{!r} does not exist".format(arg))
    if not os.path.isdir(arg):
        raise argparse.ArgumentTypeError("{!r} is not a directory".format(arg))
    return arg


ARGS = argparse.ArgumentParser(description="Run all unittests.")
ARGS.add_argument(
    '-x', '--exitfirst', action="store_true", default=False, dest='failfast',
    help='stop after the first non-successful result')
ARGS.add_argument(
    '-c', '--catchbreak', action="store_true", default=False, dest='catchbreak',
    help='catch control-C and display results')
ARGS.add_argument(
    '--forever', action="store_true", dest='forever', default=False,
    help='run tests forever to catch sporadic errors')
ARGS.add_argument(
    '-z', '--random', dest='seed', action='store', nargs='?', type=int,
    const=randrange(10000000), metavar='seed',
    help='run tests in random order using the specified seed')
ARGS.add_argument(
    '-d', '--directory', metavar='test-dir', action="store", dest='testsdir',
    default='tests', type=directory,
    help='specify the directory where tests are located')
ARGS.add_argument(
    '-v', action="store", dest='verbose', metavar='0,1,2,3,4', nargs='?',
    type=int, const=1, default=0, help='verbose mode')
ARGS.add_argument(
    'pattern', nargs='?', action='store', default='test*.py',
    help='load only test files that match pattern')


def randomize_tests(tests, seed):
    random.seed(seed)
    print("Using random seed", seed)
    random.shuffle(tests._tests)


def main(argv=None):
    args = ARGS.parse_args(argv)
    logging.getLogger().setLevel(level(args.verbose))
    if args.catchbreak:
        installHandler()
    loader = defaultTestLoader
    try:
        tests = loader.discover(args.testsdir, args.pattern)
        runner = TextTestRunner(verbosity=args.verbose, failfast=args.failfast)
        if args.forever:
            while True:
                if args.seed:
                    randomize_tests(tests, args.seed)
                result = runner.run(tests)
                if not result.wasSuccessful():
                    return 1
        else:
            if args.seed:
                randomize_tests(tests, args.seed)
            result = runner.run(tests)
            return int(not result.wasSuccessful())
    except KeyboardInterrupt:
        print('Interrupted.')
        return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
