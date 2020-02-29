from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []

    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)

            for i in range(p*2, n+1, p):
                is_prime[i]= False
    return primes

def generate_primes2(n):
    # TODO - you fill in here.
    if n==2:
        return [2]
    primes = []

    all_multiples = set()

    def get_multiples(factor, limit):
        multiples = set()
        base = factor
        while factor<=limit:
            factor += base
            multiples.add(factor)
        return multiples

    for i in range(2,n+1):
        if i in all_multiples:
            pass
        all_multiples = all_multiples.union(get_multiples(i, n))
    

    for i in range(2,n+1):
        if i in all_multiples:
            pass
        else:
            primes.append(i)

    
    """
    for x in l:
        if x %l and not count:
            count = 1
        
    """
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
