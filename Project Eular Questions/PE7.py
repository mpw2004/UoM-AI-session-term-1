count = 0
num = 1

while count < 10001:
    num += 1   # find the 10001st prime number
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:        #check whether the number is prime or not
            is_prime = False
            break
    
    if is_prime:
        count += 1

print(num)
