import prime_tools


track = []
for i in range(222281, 222382):
    binar = str(bin(i)[2:])
    for j in range(len(binar)):
        if binar[j] == '1':
            track.append(1)
    if prime_tools.is_prime(len(track)):
        print(i)
