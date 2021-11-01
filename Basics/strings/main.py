

# Creating stings

name = "Kris"
single_quotes = "Strings can be in single quotes too"


long_string = '''
This is supposed to be a very long strings 
for multiple lines 
I like this 
'''

print(long_string)

# Concatenation

first_name = "Kris"
last_name = "Thomas"
full_name  = first_name + ' ' + last_name

print(f"I just added two strings together look: {full_name}")

# Type Conversion pt 2
name = "Kris"
age = 22

print("Python will automatically change number into a string. My name is ", name, "and my age is", age, ".")

a = str(100)
b = int(a)
c = type(b)

print(c)

# String index
name = "Kris"
first_index_of_name = name[0]
second_index_of_name = name[1]
third_index_of_name = name[2]
fourth_index_of_name = name[3]

print(first_index_of_name)
print(second_index_of_name)
print(third_index_of_name)
print(fourth_index_of_name)

# strings are stored in memory as an ordered sequence of characters

#  Slicing
# [start:stop]
print(name[0:4]) # print the full string

#[start:stop:stepover]
print(name[0:4:2]) # this will print every other index "ki"
print(name[1:]) # "ris"
print(name[:4]) # "Kris"
print(name[::2]) # "Ki"

#end of the string
print(name[-4]) #s
print(name[::-1]) #reverse the string
print(name[::-2])

# Immutability - strings cannot be changed

last_name = "Johnson"
# last_name[0] = "K" -> you cannot change the string, but you can reassign the variable
last_name = 4.2
print(last_name) # 4.2


# Built in functions and methods
# https://docs.python.org/3/library/functions.html
# String methods: https://www.w3schools.com/python/python_ref_string.asp
length_of_name = len(name)
print(length_of_name)

#len does not start from 0, starts from 1

print(name.count('r')) # r shows up ones
print(name.capitalize()) # makes the first character of a string capital

sentence = "I like cats"
print(sentence.split(" ")) # separate by space, return list


# using brakets to access characters in a string
new_name = "Kris Thomas"
last_char_of_name = new_name[len(new_name) - 1]
print(last_char_of_name)
print(new_name[0:])
print(new_name[0::2])
print(new_name[::-1])
# the last 3 characters
print(new_name[-3:])

path = "profile.txt"
filetype = path[-4:]
print(filetype)


def check_substring(str, path):
    if str in path:
        return True
    else:
        return False

print(check_substring(".txt", path)) # true
print(check_substring("dog", path)) # false

