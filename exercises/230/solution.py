import prime_tools


count = 1
flag = 0
while flag is 0:
    if prime_tools.is_prime(100000000 + count):
        flag = 1
        print(100000000 + count)
    else:
        count = count+1
