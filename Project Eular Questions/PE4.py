def palindrome(n):
    '''
    this uses to check whether the number is palindrome or not
    '''
    return str(n)==str(n)[::-1]


largest=0

for i in range(999,99,-1):
    for j in range(999,99,-1):
        if palindrome(i*j) and largest<i*j: #this gives the largest palindrome 
            largest=i*j
            
            
print(largest)
