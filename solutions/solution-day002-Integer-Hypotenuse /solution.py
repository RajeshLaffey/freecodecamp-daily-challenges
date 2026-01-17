
'''
DAY 02 - Integer Hypotenuse
Given two positive integers representing the l
engths for the two legs (the two short sides) of 
a right triangle, determine whether the hypotenuse 
is an integer.

The length of the hypotenuse is calculated by adding
 the squares of the two leg lengths together and then 
 taking the square root of that total (a2 + b2 = c2).

'''
import math 
def is_integer_hypotenuse(a, b):
    c2 = a**2 + b**2
    
    c = math.isqrt(c2)
    
    if c*c == c2:
        text = "The hypotenuse is an integer"
    else:
        text = "The hypotenuse is not an integer"
        
    
    return text

test = is_integer_hypotenuse(3, 5)
test2 = is_integer_hypotenuse(3, 4)

print(test)
print(test2)
