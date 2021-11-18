
# convert two lists into a dictionary

# solution 1 - manual
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {
    'Ten': 10,
    'Twenty': 20,
    'Thirty': 30
}

print(dict1)

# solution 2 - zip() and dict()
keys1 = ['Ten', 'Twenty', 'Thirty']
values1 = [10, 20, 30]

res_dict = dict(zip(keys1, values1))
print(res_dict)

# zip() takes two or more iterables, aggregates them into a tuple, and returns the result

# Merge two dictionaries in python
dict3 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict4 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# solution 1 - iterate over one dictionary and add to the other

foreach