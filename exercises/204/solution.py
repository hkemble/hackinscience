def perfect_shuffle(deck):
    half = int(len(deck)/2)
    shuf = []
    a = deck[:half]
    b = deck[half:]
    for i in range(half):
        shuf.append(a[i])
        shuf.append(b[i])
    return shuf
