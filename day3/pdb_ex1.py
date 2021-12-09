#!/usr/bin/env python

"""
Pdb Ex1
------------

Use this pdb_ex1.py program. This program has the following added to it already:

import pdbr
pdbr.set_trace()


Execute your program and verify that you drop into the debugger.

a. List the 10 lines around your current point.

b. Execute "next" three times.

c. Print out a variable in your program

d. Execute !my_var = 72 and verify this variable is now set in your program using 'p my_var'.

e. Set a breakpoint ahead of your current point. Use 'continue' to execute and verify you are now
stopped at the breakpoint.

f. Use 'step' to descend down into a function call. Once in the function use 'up' to go up the
stack once and 'down' to descend back down the stack once.

g. Use 'args' to see the arguments that were passed into the function.

h. Use 'q' to exit the debugger.

"""


import pdbr  # noqa


def my_func(x, y, z=20):
    return x + y + z


pdbr.set_trace()
print()
return_val = my_func(10, 20, 30)
print("Calling with three positional args: {}".format(return_val))

return_val = my_func(x=10, y=20)
print("Calling with two named args: {}".format(return_val))

return_val = my_func(10, z=13, y=20)
print("Calling with one positional and two named args: {}".format(return_val))

return_val = my_func(x="x", y="y", z="z")
print("Calling with three strings: {}".format(return_val))

return_val = my_func(x=["x"], y=["y"], z=["z"])
print("Calling with three lists: {}".format(return_val))
print()

