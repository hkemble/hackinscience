import operator
from functools import reduce


def mul_2(list_num):
    return reduce(operator.mul, list_num, 1)
