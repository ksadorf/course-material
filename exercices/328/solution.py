import operator
from functools import reduce

def mul(tab):
    return reduce(operator.mul, tab, 1)
