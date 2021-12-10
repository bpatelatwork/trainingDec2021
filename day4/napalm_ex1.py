#!/usr/bin/env python

"""

Use NAPALM to connect to arista1 through arista4.

Using the "get_vlans()" method retrieve the VLAN table from each of the four
arista switches.

Use rich.print to print this VLAN table to standard output.

"""

from rich import print
from napalm import get_network_driver

#Arista device definitions are stored in external Python module so that they can be re-used in both exercises.
from my_devices import arista1, arista2, arista3, arista4


if __name__ == "__main__":
    print()
    for device in [arista1, arista2, arista3, arista4]:
        driver = get_network_driver("eos")
        with driver(**device) as device:
            device.open()
            vlans = device.get_vlans()
            host = device.hostname

        print()
        print("-" * 80)
        print(f"Host: {host}")
        print("-" * 12)
        print(vlans)
        print("-" * 80)
        print()

    print()

