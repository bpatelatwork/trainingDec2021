#!/usr/bin/env python

"""

Using the Python requests library. Connect to the following URL 
(https://netbox.lasthop.io/api) and retrieve the information there using an
HTTP GET.

You will probably need the following HTTP Headers:

http_headers = {"accept": "application/json; version=2.4;"}

This is a public endpoint -- meaning that there is no authentication
necessary to execute a "GET" against it.

Use the "dir()" function to print out the attributes/methods of the response.

Print out some of the useful attributes of the response object.

What is "useful" will be up to you, but commonly used attributes include:
.text, .json(), .ok, and .status_code. 

"""

import requests
from rich import print
from urllib3.exceptions import InsecureRequestWarning

# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def main():
    url = "https://netbox.lasthop.io/api/"

    #API works even without it but hardcoded to have remote netbox v2.4 send response in json
    http_headers = {"accept": "application/json; version=2.4;"}

    #need verify=False or it failes because cert error
    response = requests.get(url, headers=http_headers, verify=False)

    print()
    print(dir(response))
    print()
    print(response.text)
    print()
    print(response.json())
    print()
    print(response.ok)
    print()
    print(response.status_code)


if __name__ == "__main__":
    main()

