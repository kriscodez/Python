##int

##integer - whole number, no decimals
print(2+4)
print(2-4)
print(2*4)
print(2/4)

## Type - shows the data type
print(type(2+4)) ## <class 'int'>


##float - floating point number, number with a decimal point
print(type(0.001)) ## <class 'float'>

## floats take up more memory than integers
## so you need to differentiate between the type
## so that the machine is able to store it properly
## decimals are hard to represent in binary, so the
## computer actually stores it in two different places

## Python will do automatic type conversion
print(type(9.9+1.1)) ## this equals 11.0, so it will still be a float

#exponents in python
print(2**3)

# returns an integer rounded down
print(2//4)

# modulo - we know about this already. Returns the remainder.
print(5%4)

#### MATH FUNCTIONS ####
## Documentation: https://docs.python.org/3/library/math.html
print(round(3.1)) ## this rounds down to the nearest int
print(abs(-20)) ## returns the absolute value



## Operator Precedence

print(20 - 3 * 4)

#() - Parentheses
#** - Exponents
# * / - multi/div
# + - - addition/subtraction