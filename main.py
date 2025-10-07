def print_christmas_tree(x):
    for i in range(1, x + 1):
        spaces = ' ' * (x - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def is_subsequence(x0, y0):
    index = 0
    for ch in y0:
        if index < len(x0) and x0[index] == ch:
            index += 1
    return index == len(x0)

# Example usage
print_christmas_tree(10)
print(is_subsequence("apple", "adcsjncjsppaxjjnaxle"))  # True
print(is_subsequence("apple", "bsdpple"))               # False
print(is_subsequence("apple", "paple"))                 # False
