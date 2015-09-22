import prime_tools


track = []
for i in range(10000, 10050):
    if prime_tools.is_prime(i):
        track.append(i)
print(", ".join(str(j) for j in track))
