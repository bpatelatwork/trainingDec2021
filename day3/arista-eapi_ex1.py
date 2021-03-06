#!/usr/bin/env python

"""

Exercise1
-----

Using the Arista pyeapi library make a connection to the Arista1 through Arista4
switches.

From each of these switches retrieve the "show lldp neighbors" table.

From the returned data structure extract only the LLDP neighbor table and
print the hostname and the corresponding LLDP table to standard output.

Your output should look similar to the following (note the arista switches have
parallel connections to each other).


Host: arista1.lasthop.io
[
    {'ttl': 120, 'neighborDevice': 'arista2', 'neighborPort': 'Ethernet2', 'port': 'Ethernet2'},
    {'ttl': 120, 'neighborDevice': 'arista2', 'neighborPort': 'Ethernet3', 'port': 'Ethernet3'},
    {'ttl': 120, 'neighborDevice': 'arista2', 'neighborPort': 'Ethernet4', 'port': 'Ethernet4'},
    {'ttl': 120, 'neighborDevice': 'arista2', 'neighborPort': 'Ethernet5', 'port': 'Ethernet5'},
    {'ttl': 120, 'neighborDevice': 'arista2', 'neighborPort': 'Ethernet6', 'port': 'Ethernet6'},
    {'ttl': 120, 'neighborDevice': 'arista2', 'neighborPort': 'Ethernet7', 'port': 'Ethernet7'}
]
--------------------------------------------------------------------------------

Host: arista2.lasthop.io
[
    {'ttl': 120, 'neighborDevice': 'arista1', 'neighborPort': 'Ethernet2', 'port': 'Ethernet2'},
    {'ttl': 120, 'neighborDevice': 'arista1', 'neighborPort': 'Ethernet3', 'port': 'Ethernet3'},
    {'ttl': 120, 'neighborDevice': 'arista1', 'neighborPort': 'Ethernet4', 'port': 'Ethernet4'},
    {'ttl': 120, 'neighborDevice': 'arista1', 'neighborPort': 'Ethernet5', 'port': 'Ethernet5'},
    {'ttl': 120, 'neighborDevice': 'arista1', 'neighborPort': 'Ethernet6', 'port': 'Ethernet6'},
    {'ttl': 120, 'neighborDevice': 'arista1', 'neighborPort': 'Ethernet7', 'port': 'Ethernet7'}
]
--------------------------------------------------------------------------------

Host: arista3.lasthop.io
[
    {'ttl': 120, 'neighborDevice': 'arista4', 'neighborPort': 'Ethernet2', 'port': 'Ethernet2'},
    {'ttl': 120, 'neighborDevice': 'arista4', 'neighborPort': 'Ethernet3', 'port': 'Ethernet3'},
    {'ttl': 120, 'neighborDevice': 'arista4', 'neighborPort': 'Ethernet4', 'port': 'Ethernet4'},
    {'ttl': 120, 'neighborDevice': 'arista4', 'neighborPort': 'Ethernet5', 'port': 'Ethernet5'},
    {'ttl': 120, 'neighborDevice': 'arista4', 'neighborPort': 'Ethernet6', 'port': 'Ethernet6'},
    {'ttl': 120, 'neighborDevice': 'arista4', 'neighborPort': 'Ethernet7', 'port': 'Ethernet7'}
]
--------------------------------------------------------------------------------

Host: arista4.lasthop.io
[
    {'ttl': 120, 'neighborDevice': 'arista3', 'neighborPort': 'Ethernet2', 'port': 'Ethernet2'},
    {'ttl': 120, 'neighborDevice': 'arista3', 'neighborPort': 'Ethernet3', 'port': 'Ethernet3'},
    {'ttl': 120, 'neighborDevice': 'arista3', 'neighborPort': 'Ethernet4', 'port': 'Ethernet4'},
    {'ttl': 120, 'neighborDevice': 'arista3', 'neighborPort': 'Ethernet5', 'port': 'Ethernet5'},
    {'ttl': 120, 'neighborDevice': 'arista3', 'neighborPort': 'Ethernet6', 'port': 'Ethernet6'},
    {'ttl': 120, 'neighborDevice': 'arista3', 'neighborPort': 'Ethernet7', 'port': 'Ethernet7'}
]
--------------------------------------------------------------------------------

"""

import pyeapi
from getpass import getpass
from rich import print

password = getpass()
base_dict = {
    "transport": "https",
    "username": "pyclass",
    "password": password,
    "port": "443",
}

arista1 = base_dict.copy()
arista1["host"] = "arista1.lasthop.io"
arista2 = base_dict.copy()
arista2["host"] = "arista2.lasthop.io"
arista3 = base_dict.copy()
arista3["host"] = "arista3.lasthop.io"
arista4 = base_dict.copy()
arista4["host"] = "arista4.lasthop.io"

print()
for device_dict in (arista1, arista2, arista3, arista4):
    conn = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(conn)
    output = device.enable(["show lldp neighbors"])
    print()

    #print(f"Host: {device_dict['host']}")
    #print(output[0]["result"]["lldpNeighbors"])
    
    # my modification
    localdevice = "Local Device"
    localport = "Local Port"
    neighbordevice = "Neighbor Device"
    neighborport = "Neighbor Port"

    neighbors = output[0]["result"]["lldpNeighbors"]
    
    print(f"{localdevice:^20} {localport:^20} {neighbordevice:^20} {neighborport:^20}")
 
    for neighbor in neighbors:
        print(f"{device_dict['host']:^20} {neighbor['port']:^20} {neighbor['neighborDevice']:^20} {neighbor['neighborPort']:^20}")

    print("-" * 80)

print()

