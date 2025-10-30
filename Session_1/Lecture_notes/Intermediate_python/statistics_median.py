import statistics
data = [1, 3, 3, 6, 7, 8, 9]
for i in range(len(data)):
    new_list= data[:i+1]
    median = statistics.median(new_list)
    print(f"Median of {new_list} is {median}")

#calculating the changing median as we add more data points
import statistics
data = [1, 3, 3, 6, 7, 8, 9]
for i in range(len(data)):
    new_list= data[:i+1]
    median = statistics.median(new_list)
    print(f"Median of {new_list} is {median}")