#!/usr/bin/env python

"""

Functions Ex1
--------------

a. Construct a function that has three parameters x, y, z
b. z has a default value of 20
c. Return x + y + z
d. Call this function using all three positional arguments
e. Call this function using named arguments x, y (let z be the default)
f. Call this function with one positional argument and two named arguments.
g. Call this function using three strings.
h. Call this function using three lists.

"""

def myfunction(x, y, z=20):
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"z is {z}")
    return x + y + z


print("\n\nexecute d:")
d = myfunction(10, 20 , 30)
print(f"x + y + z is: {d}\n\n")

print("#"*60)
print("\n\nexecute e:")
e = myfunction(x=1, y=2)
print(f"x + y + z is: {e}\n\n")

print("#"*60)
print("\n\nexecute f:")
f = myfunction(11, z=22, y=33)
print(f"x + y + z is: {f}\n\n")

print("#"*60)
print("\n\nexecute g:")
g = myfunction('a', 'b', 'c')
print(f"x + y + z is: {g}\n\n")

print("#"*60)
print("\n\nexecute h:")
h = myfunction([1,2], [3,4], [5,6])
print(f"x + y + z is: {h}\n\n")


