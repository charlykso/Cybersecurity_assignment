#!/usr/bin/python3

import sys
import re
import subprocess


def ip_finder(interface):
    try:
        result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.STDOUT).decode('utf-8')
        ip_parttern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        ip_address = ip_parttern.findall(result)

        if ip_address:
            return ip_address[0]
        else:
            raise valueError("Ip address not found")
    except subprocess.CalledProcessError as e:
        print(f"Error fetching Ip address: {e}")
        return none

def main():
    if len(sys.argv) != 2:
        print("Usage: ./ip_finder.py <interface>")
        sys.exit(1)

    interface = sys.argv[1]

    print(f"Ip address: {ip_finder(interface)}")

if __name__ == "__main__":
    main()

