#!/usr/bin/env python3


import subprocess
import optparse

def get_arguments():  #This is to get the argument from the user
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest= "interface", help="Interface to change MAC Address")
    parser.add_option("-m", "--mac", dest="mac_add", help="Specify the new mac address")

    return parser.parse_args()


def change_mac(interface, mac_add):  #This will be used to change the MAC Address
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_add])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


(options, argument) = get_arguments()
change_mac(options.interface, options.mac_add )#Call a function is basically the same as using, be sure to call the the variables
