limit = 2000000
total = 0

for num in range(2, limit):
    # find the sum of all primes below two million
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total += num

print(total)   #output the result 
