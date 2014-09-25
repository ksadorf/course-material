import numpy as np
import timeit
from distance import *


def benchmark(funcs, a, b):
        res = {}
        for f in funcs:
                t = timeit.Timer(lambda: f(a, b))
                res[f.__name__] = t.timeit(number=10)
        return res
