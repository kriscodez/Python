
# Lists

li = [1,2,3,4,5]
li2 = ["a", "b", "c"]
li3 = [1,2, bool, 'a']

# List is a data structure. Data structure is a way for us to contain and organize data

# List Indexing
amazon_cart = ['notebook', 'apple ipad']
print(amazon_cart[0])
print(amazon_cart[1])

# List Slicing - works like string slicing
# Slicing creates a new list, it does not alter the original list
# lIsts are mutable
amazon_cart = [
    'notebook',
    'apple ipad',
    'pens',
    'paper',
    'grapes',
    'granola'
]

#print all of the items in the list
print(amazon_cart[0:])

#print the first two items in the list
print(amazon_cart[0:2])

#print the last two items in tht list
print(amazon_cart[:3:-1])

# print every other item in the list, starting with the first, increment by two
print(amazon_cart[0:len(amazon_cart):2])

# print every other item in the list, starting with the second, increment by two
print(amazon_cart[1:len(amazon_cart):2])

# REASSIGN an index in the list
amazon_cart[0] = 'Toolkit'

# Copy a list
new_list = amazon_cart[:]
print("New List: ", new_list)

## MATRIX - List Within a List

A = [
    [1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]
]
# full matrix
print ("A = ", A)

# 2nd row
print("Second row: ", A[1])
# 3rd element of second row
print("3rd elem of second row: ", A[1][2])
# last element of first row
print("Last elem of first row: ", A[0][3])


# creating an empty list
new_column = []
#adding to exisitng list
#A.append(new_column)
#print result
print ("A matrix with new, empty column = ", A)

## for each row in A, append the 3rd elem to the new column
for row in A:
    new_column.append(row[2])

#print result
print("new column filled in: ", new_column)

#LIST METHODS: https://www.w3schools.com/python/python_ref_list.asp
num_list = [3, 4, 5, 6, 7, 9]

#add to the end of the list
num_list.append(5)
print("List with appended value: ", num_list)

# return the index of a given value
print(num_list.index(4)) #1

#insert - adds elem to a specific index
# index, value - insert at index 3, value 2
num_list.insert(3, 2)
print("New index with inserted value: ", num_list)

#pop - removes elem at specified position
num_list.pop(len(num_list) - 1) # removed the last item
print("List after removing the last item: ", num_list)

# create a list based on a range
list_1_to_50 = list(range(1, 50))
print(list_1_to_50)

# join
sent = " "
sent = sent.join(["hi", "my", "name", "is", "kris"])
print(sent)

#better way to do so
join_example = ''.join(["hello", "world"])

# list unpacking - assigning a list of variables to each elem of a list
a, b, c = [1, 2, 3]

print(a)
print(b)
print(c)

# assign the first few elements to variables, keep rest of list in tact, assign to list named "rest"
d, e, f, *rest = [1, 2 , 3, 4, 5, 6]
print(*rest)

print(round(12.54, 2))