#!/usr/bin/env python

"""

Create a Python program that creates a PyEZ Device connection to "vmx2". 

Using this PyEZ connection and the RouteTable and ArpTable views retrieve the 
routing table and the arp table for vmx2.

As part of this program create at least two functions:

function1:
-----
def gather_routes(device):

Takes a Juniper PyEZ device object and returns the route table from the
RouteTable view.

===
routes = RouteTable(device)
routes.get()
return routes
===


function2:
-----
def gather_arp_table(device):

Takes a Juniper PyEZ device object and returns the ARP table from the
ArpTable view.

"""

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from getpass import getpass
from rich import print


def getroutetablefrom(device):
    print(device)
    routes = RouteTable(device)
    routes.get()
    return routes


#myjuniper = {'device_type': 'juniper_junos', 'host': 'vmx2.lasthop.io', 'username': 'pyclass', 'password': getpass()}
myjuniper = {'device_type': 'juniper_junos', 'host': 'vmx2.lasthop.io', 'user': 'pyclass', 'password': '88newclass'}

myjuniperconn = Device(**myjuniper)
#print(dir(myjuniperconn))

myjuniperconn.open()

routes = getroutetablefrom(myjuniperconn)
#print(type(routes))
print(routes.items())


