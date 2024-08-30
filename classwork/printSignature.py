#!/usr/bin/python

import re
import subprocess
import sys

def printSig():
    print('''

    ***  ***        ******.
    * *  * *  ***   * ****'
    * *  * *." *    * *    
    * *  * * *      * ****.
    * *  * *  *     * ****'
    * *  * * * *    * *   
    * *  * *  * *   * ****.
    ***  ***   ***  ******'

    
    ''')

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            return f"[-] No Mac address found in this interface : {interface}" 
    except:
        return f"[-] No Mac address found in this interface: {interface}"

def change_mac_address(interface, new_mac, initial_mac):
    try:
        print(f"[-] Changing Mac Address for {interface}, from {initial_mac}, to {new_mac}...")
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
        print("[-] Mac Address changed...")
    except:
        print("[-] An error occured")

def main():
    printSig()

    argv = sys.argv
    if len(argv) != 3:
        print("Error: Useage; ./filename interface mac")
        return -1
    interface = argv[1]
    new_mac_address = argv[2]
    initial_mac = get_current_mac(interface)
    change_mac_address(interface, new_mac_address, initial_mac)


if __name__ == "__main__":
    main()

