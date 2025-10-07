n=0 # consider the all natural numbers staring from 0
total=0 #to takes the sum of multiplies of 3 or 5
while n<1000: #consider natural numbers till 1000
    if n%3==0 or n%5==0: 
        total+=n # takes the sum
    n+=1

print(total) # output the total
        
