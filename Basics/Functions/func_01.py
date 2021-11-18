
"""
if two arguments are passed, then return the product. If one is passed then just return that argument.
"""
def mult(a, b = None):
    if b is not None:
        print(a * b)
    else:
        print(a)

mult(3, 2)

mult(2)

"""
unpacking arguments using *
The method below assumes that all of the arguments are strings
"""

def printNames(*names):
    for name in names:
        print(f"Hello {name}!")


printNames("Kris","Bill", "Andrew", "Rebecca", "Kaitlyn", "Ronald")