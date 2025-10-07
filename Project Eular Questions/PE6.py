n = 100

sum_of_squares = 0     # sum of squares

for i in range(1, n + 1):
    sum_of_squares += i * i

sum_natural = 0        # square of sum

for i in range(1, n + 1):
    sum_natural += i
    
square_of_sum = sum_natural * sum_natural

difference = square_of_sum - sum_of_squares  # calculate the difference

print(difference)
