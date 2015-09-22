import prime_tools


for i in range(222281, 222381):
    track = []
    binar = str(bin(i)[2:])
    for j in range(len(binar)):
        if binar[j] == '1':
            track.append(1)
    if prime_tools.is_prime(len(track)):
        print(i)
