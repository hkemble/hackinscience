def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n & 1 == 0:
        return False
    else:
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
    return True
