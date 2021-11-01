
import math

# Print the highest even number in a list of numbers
"""
def highest_even(even_numbers):
    count = 0;
    i = 0
    highest_num = even_numbers[0]

    while i <= len(even_numbers):
        if even_numbers[i] < even_numbers[i + 1]:
            highest_num = even_numbers[i + 1]
        else:
            highest_num = even_numbers[i]
        i += 1
    return  highest_num



print(highest_even([2, 4, 6, 8]))
"""

""" Generalization """

def area_squre(r):
    assert r > 0,  'The length must be positive'
    return r * r

def area_circle(r):
    return r * r * pi

def area_hexagon(r):
    return r * r * 3 * sqrt(3) / 2

# assign a function to a variable does not call the function, rather creates a reference to the function

def add(a, b):
    return a+b

assignment = add
# actual function call
print(add(1, 2)) # 3

# function reference 
print(assignment(1, 2)) # 3