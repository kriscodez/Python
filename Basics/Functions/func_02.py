def f():
    print(x)
def g():
    print(x)
    x = 1

x = 3
f() # f is able to print x as normal, we're using the outside version of x
x = 3
g() # x is defined in the scope of the function, which means we're using that local variable. An error is thrown because
# x is printed before it exists within the scope of g
