#!/usr/bin/env python

"""

Functions Ex2
--------------

Expand on functions exercise 1.

a. Create a list with three numbers
b. Use *args to call the function
c. Create a dictionary that has three keys of x, y, and z
d. Call the functions using **kwargs

"""

def myfunction(x, y, z=20):
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"z is {z}")
    return x + y + z

alist = [1, 2, 3]

adict = {'x': 11, 'y': 22, 'z':33}


print(f"\n\nCalling Function Using a list: {alist}")
callFunctionUsing_alist = myfunction(*alist)
print(callFunctionUsing_alist)
print('#'*60)

print(f"\n\nCalling Function Using a list: {adict}")
callFunctionUsing_adict = myfunction(**adict)
print(callFunctionUsing_adict)
print('#'*60)

