#!/usr/bin/env python

"""
Using Arista'a pyeapi library configure three VLANs on one of the Arista
switches. Choose three VLAN numbers in the 600 to 899 range. Additionally, 
assign each of these VLANs a VLAN name.

Execute "show vlan" after your configuration is done and print this output
to standard output.

Verify your three new VLANs and corresponding names are in the "show vlan"
output.

"""

import pyeapi
from getpass import getpass
from rich import print


cfg = [
    "vlan 800",
    "name blue800",
    "vlan 801",
    "name blue801",
    "vlan 802",
    "name blue802",
]

connection = pyeapi.client.connect(
    transport="https",
    host="arista1.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
cfg_output = device.config(cfg)

output = device.enable(["show vlan"])
print(output)

