import os
import sys

from itertools import chain, islice


BLOCKSIZE = 4096


def split(filename, size):
    '''Split a file into pieces.

    Output fixed-size pieces of input file to filename.1, filename.2, etc.
    Believe it or not, this Python version competes with the Unix split(1)
    command (tests performed on files up to 10 GB), thanks to the use of
    generators.
    '''
    try:
        fsinfo = os.statvfs(filename)
        bsize = fsinfo.f_bsize
    except AttributeError:
        bsize = BLOCKSIZE

    def chunks(fd, num_chunks):
        iterable = iter(lambda: fd.read(bsize), b'')
        while True:
            yield chain([next(iterable)], islice(iterable, num_chunks))

    num_chunks = max(size, bsize) / bsize
    with open(filename, 'rb') as src_file:
        for i, src_chunks in enumerate(chunks(src_file, num_chunks)):
            split_filename = '{}.{}'.format(filename, i)
            with open(split_filename, 'wb') as dst_file:
                for chunk in src_chunks:
                    dst_file.write(chunk)
