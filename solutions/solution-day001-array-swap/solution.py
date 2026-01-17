'''
DAY 01 - ARRAY SWAP
Given an array with two values, return an array with the values swapped.
'''

def array_swap(arr):
    a, b = arr
    arr = [b, a]
    
    return arr

print(array_swap(["A", "B"]))     # strings
print(array_swap([1, 2]))         # integers
print(array_swap(["A", 10]))      # mixed types
print(array_swap([True, None]))

