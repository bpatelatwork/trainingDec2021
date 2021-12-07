#!/usr/bin/env python

"""
String Ex1
----------

### Work in your pynet_test repository ###

a. Create a python script with three strings representing three names
b. Print these three names out in a column 30 wide, right aligned
c. Execute the script verify the output
d. Add a prompt for a fourth name, print this out as well
e. check your code into GitHub
"""


str1 = "name1"
str2 = "name2"
str3 = "name3"
str4 = input("Enter the forth string: ")

print(f"{str1:>30} {str2:>30} {str3:>30} {str4:>30}")

