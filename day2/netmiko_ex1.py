#!/usr/bin/env python

"""

Netmiko Ex1
-----------

Write a Netmiko script that connects to one Arista switch and one Juniper vMX.
a. Print the current prompt
b. use send_command to retrieve 'show version' from the two devices. 
c. use send_command to retrieve running configuration from the two devices. 
d. Save the running config to a file.


Dictionary for network devices that can be used with Netmiko.

    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": std_password,
    }

    vmx1 = { 
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": std_password,
    }

"""

from netmiko import ConnectHandler

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",}
#print(arista1)

vmx1 = { 
    "device_type": "juniper_junos",
    "host": "vmx1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",}

#print(vmx1)


for device in [arista1, vmx1]:
    netconnect = ConnectHandler(**device)
    
    prompt = netconnect.find_prompt()
    print(prompt)

    version = netconnect.send_command("show version")
    print(version)
    
    if device["device_type"] == "arista_eos":
        config = "show runn"
    elif device["device_type"] == "juniper_junos":
        config = "show configuration"
    
    config = netconnect.send_command(config)
    #print(config)
    
    print("#"*60)
    netconnect.disconnect()
    
    with open (f"{netconnect.base_prompt}.txt", "w") as f:
        f.write(config)


