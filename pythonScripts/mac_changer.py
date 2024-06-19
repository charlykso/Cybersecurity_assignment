#!/usr/bin/python3

import subprocess
import sys
import re

def get_current_mac(interface):
    try:
        result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.STDOUT).decode("utf-8")
        mac_search = re.search(r'(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)', result)

        if mac_search:
            return mac_search.group(0)
        else:
            raise valueError("Mac address not found")
    except subprocess.CalledProcessError as e:
        print("Error fetching mac address: {e}")
        return none

def change_mac(interface, new_mac):
    try:
        subprocess.checkall(["sudo", "ifconfig", interface, "down"])
        subprocess.checkall(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.checkall(["sudo", "ifconfig", interface, "up"])
        print(f"Mac address for {interface} changed to {new_mac}")
    except subprocess.CalledProcessError as e:
        print("Failed to change mac address: {e}")
        return none

def main():
    if len(sys.argv) != 3:
        print("Usage: sudo python3 mac_change.py <interface>")
        sys.exit(1)

    interface = sys.argv[1]
    new_mac = sys.argv[2]

    print(f"Current mac address: {get_current_mac(interface)}")


    change_mac(interface, new_mac)
    print(f"New mac address: {get_current_mac(interface)}")


if __name__ == "__main__":
    main()

