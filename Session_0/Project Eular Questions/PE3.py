def largest_prime_factor(n):
    '''
    this uses to find the largest prime factor of a number
    '''
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor  # divide out factor
        else:
            factor += 1
    return n  # the remaining n is the largest prime factor

num = 600851475143
print(largest_prime_factor(num))
    
