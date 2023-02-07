def Lucas_Lehmer_test(p):
    """
    Takes as an input an odd prime number p.
    Returns True if the p-th Mersenne number 2**p - 1 is prime.
    Otherwise, returns False.
    """
    Mp = 2**p - 1
    s = 4
    for i in range(p - 2):
        s = (s * s - 2) % Mp
    return s == 0
