#!/usr/bin/env python

"""

PyEZ basic connection and facts:

Create a PyEZ Device object from the jnpr.junos Device class. 
This device object should connect to "vmx1.lasthop.io".

Use getpass() to enter the device's password.

rich.print all of the device's facts. 

Additionally, retrieve and print only the "hostname" fact.

"""

from jnpr.junos import Device
from getpass import getpass
from rich import print

#myjuniper = {'device_type': 'juniper_junos', 'host': 'vmx1.lasthop.io', 'username': 'pyclass', 'password': getpass()}
myjuniper = {'device_type': 'juniper_junos', 'host': 'vmx1.lasthop.io', 'user': 'pyclass', 'password': '88newclass'}

myjuniperconn = Device(**myjuniper)
myjuniperconn.open()

facts = myjuniperconn.facts

print(f"Returned facts data type is : {type(facts)}")
#print(dict(facts))

facts = dict(facts)
#print(facts.keys())

print(f"Connected device's hostname is: {facts['hostname']}")





