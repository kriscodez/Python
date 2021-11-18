# similar to lists, but they're immutable
# once an element is inside a tuple, it cannot be reassigned
# tuples use parenthesis


t = (1,2,3)
my_list = [1, 2, 3]
# tuples only have two methods
t.index(2)
t.count()

len(t) # 3
print(t[0]) # can access an index
print(t[1:]) # interesting, this returns a tuple
t.index(1) # returns the index of the first occurance of an element

#tuples can ensure data integrity
# tuples can be concatenated, but that would make a new tuple in memory

