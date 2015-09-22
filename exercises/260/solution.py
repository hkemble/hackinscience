import math


import numpy as np


def euclidean(a, b):
    d = []
    for i in range(len(a)):
        d.append((b[i] - a[i]) ** 2)
    return (sum(d)) ** 0.5


def opt_euclidean(a, b):
    d = []
    for i in range(len(a)):
        d.append(math.pow(b[i] - a[i], 2))
    return math.sqrt(math.fsum(d))


def np_euclidean(a, b):
    d = []
    for i in range(len(a)):
        d.append(np.power(b[i] - a[i], 2))
    return np.sqrt(np.sum(d))
