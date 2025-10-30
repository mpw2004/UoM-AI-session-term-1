def gcd(a, b):
    '''
    This uses to find the greates common divisor of two numbers
    '''
    
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    '''
    This uses to find whether the number divides from 1 to 20
    '''
    return a // gcd(a, b) * b

result = 1
for x in range(1, 21):
    result = lcm(result, x) #this gives the samllest value

print(result)  
