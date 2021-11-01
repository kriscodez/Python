# functional programming is about separation of concerns. Each part concerns itself with the one thing that it is good at
# data and functions are separated, unlike OOP paradigm
# functions operate on well defined data structures


# clear
# easy to extend
# easy to maintain
# DRY
# Efficient
# based on one concept called pure functions
# what is a pure function? 1) it will return the same output for a given input everytime 2) function should not produce any side effects - everything necessary is contained within the function
# pure functions is a guideline, not an absolute. It's impossible to have pure functions everywhere.

from functools import reduce

def concat_strings(str1, str2):
    return f"{str1} + {str2}"

# map, filter, zip, and reduce
# pass in the action, and the data you want to act upon

def multiply(x):
    return x * 2


print(list(map(multiply, [1, 2, 3])))

# filter - self explanatory
def only_odd(x):
    return x % 2 != 0 # evaluates to a boolean


print(list(filter(only_odd, [1, 2, 3]))) # only returns the numbers that are odd

# zip - zips 2 iterables

list1 = [10, 20, 30]
list2 = [30, 50, 60]

print(list(zip(list1, list2))) # returns tuples of data - very powerful tool

# reduce - takes the function, the sequence, the initial
# reduce: https://realpython.com/python-reduce-function/#getting-started-with-pythons-reduce
def accumulator(acc, item):
    # accumulator defaults to 0
    return acc + item

print(reduce(accumulator, list2, 0)) # returns 140
# i set the initial to 0, which is the first index of the iterable in this case.
# it added all of the
