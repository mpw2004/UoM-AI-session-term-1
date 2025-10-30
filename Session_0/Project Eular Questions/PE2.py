def fib(n):
    '''
    this function uses to calculate the Fibonacci sequence in recursive way
    '''
    
    if n==1:
        fi=1 
    elif n==2:
        fi=2
    else:
        fi=fib(n-1)+fib(n-2) # calculating the fib number 

    return fi

i=1 #stating form 1 untill the condition satisfy
total=0 # to calculate the sum of even numbers

while fib(i)<=4000000: # calculate the sum 
    if fib(i)%2==0:
        total+=fib(i)
    i+=1
    
print(total) # output the result
    


