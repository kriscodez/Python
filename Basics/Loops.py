'''
While loops: block statement that repeatedly executes until a condition is satisfied

while expression:
    statement(s)
'''

# python uses indentation to denote code blocks
count = 0
while(count < 5):
    count+=1
    print("Count is: ", count)

# using else with while loops
# else portion executes only when the while condition becomes false
count = 10
while(count >= 0):
    print("Count is: ", count)
    count -= 1
else:
    print("Count down is finished")

'''
For In Loop: Used for sequential traversal, like traversing list, string, or array 
Similar to for each loop

for iterator_var in sequence:
    statement(s)
    
'''

# Iterate over range and iterators
n = 10
for i in range(0, n):
    print(i)


#iterate over a list
# this prints all of the names in the list, no need to access the name by index
people = ["Kris", "George", "Zach", "Rachel"]
for elem in people:
    print(elem)

#Iterate over a string
name = "Kris"
for char in name:
    print(char)