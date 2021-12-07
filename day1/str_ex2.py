#!/usr/bin/env python

"""

Strings Ex2
-----------

Create a python script that prompts for an IP address.
Use #! at top of file; make executable
split on '.'      
Print out four octets with column width of 12; left aligned.
Check your code into github

"""

ip = input("Enter an IP address: ")
ipsplit = ip.split(".")


print(f"{ipsplit[0]:<12} {ipsplit[1]:<12} {ipsplit[2]:<12} {ipsplit[3]:<12}")

