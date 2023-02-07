import math

def naive_primality_test(n):
    """
    Takes as an input an integer n >= 2.
    Returns True if the integer is prime, False otherwise.
    """
    top = min(n, math.ceil(math.sqrt(n)) + 1)
    for i in range(2, top):
        if n % i == 0:
            return False
    return True
