from itertools import zip_longest
import numpy


def euclidean(a, b):
    if len(a) != len(b):
        return -1
    t = 0
    for u, v in zip(a, b):
        t += (v - u) ** 2
    return t ** .5


def opt_euclidean(a, b):
    return euclidean(a, b)


def np_euclidean(a, b):
    na = numpy.array(a)
    nb = numpy.array(b)
    return numpy.linalg.norm(na - nb)
