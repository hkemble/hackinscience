def love_meet(b, a):
    return set.intersection(set(b), set(a))


def affair_meet(c, d, e):
    return set.difference(set.intersection(set(d), set(e)) - set(c))
