
import math

#Dictionaries

dictionary = {
    'a': 1,
    'b': 2,
    'kris': 'Thomas'
}

# dictionaries are unordered key-value pair. So it's not store contiguously in memory
# The computer grabs the values based on the key
# dictionary keys must be something immutable
print(dictionary['a'])

contacts = [
    {
        "name": "Kresteanna Thomas",
        "age": 22,
        "hobbies": ["programming", "basketball", "stuntin like my daddy"]
    },
    {
        "name": "John Doe",
        "age": 54,
        "hobbies": ["boating", "reading"]
    },
    {
        "name": "Jane Parker",
        "age": 38,
        "hobbies": []
    }
]

print(contacts[0].get("name"))

# favorite_color attribute does not exist, so add default value, which is blue
print(contacts[0].get("favorite_color", "blue"))

# get everyone's name

for p in contacts:
    print(p.get('name'))


#Tuple - immutable lists. Can't sort them or reverse them.
# Best Resource: https://openbookproject.net/thinkcs/python/english3e/tuples.html
# faster than lists
new_tuple = (1, 2, 3, 4)
print(2 in new_tuple) #
print(new_tuple[1:2])
print(new_tuple[0::])
print(new_tuple.count(1)) #count returns the number of times a specified value shows up in a tuple

#tuple packing, unpacking

kris = ("ETL Developer", "1 Year", "SnapLogic") # here we're assigning the values to kris
(role, experience, specialty) = kris # here we're assigning those values, represented as kris, to the variables on the left

print(role) # return ETL Developer

# tuples can be used on fuctions to return multiple values

def f(r):
    ''' Return (circumference, area) of a circle of radius r '''
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (round(c, 2), round(a, 2))

print(f(2))


# Sets - unordered collection of unique objects

new_set = {1, 2, 3, 4, 5}
print(1 in new_set)

# Important note!
#The Equality operator (==) compares the values of both the operands and checks for value equality. Whereas the 'is' operator checks whether both the operands refer to the same object or not

# Enumerate will iterate over each item and can also give the value at that index
for i, char in enumerate('Hello'):
    print(i, char)

# if the "i" is not there, it returns tuples for each iteration
for i, num in enumerate([3, 5, 6]):
    print(i, num)



picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
   for item in row:
       if item == 0:
           print(" ")
       else:
           print("*")
    print()