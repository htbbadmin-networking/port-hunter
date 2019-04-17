#!/usr/bin/python3

from __future__ import print_function

import argparse
import napalm
import os
import sys

from napalm import get_network_driver
from getpass import getpass

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Print Verbose Output", action="store_true")
    parser.add_argument("-s", "--start-ip", help="IP Address of switch/router to start search")
    parser.add_argument("-l", "--locate-ip", help="IP address of unlocated host")
    parser.add_argument("-u", "--username", help="SSH Username")
    parser.add_argument("-d", "--driver", help="Network Driver", type=str, choices=["eos", "iosxr", "junos", "nxos", "ios"], default = "ios")
    parser.add_argument("-r", "--retries", help="Number of retries", type=int, default=3)
    args = parser.parse_args()
    args_dict = args.__dict__
    for key in args_dict.keys():
        if args_dict[key] == None:
            newvalue = input("Please specify " + key + ": ")
            setattr(args, key, newvalue)
    return args

def sanity_check(args):
    return

def init_device(address, username):
    driver = get_network_driver('ios')
    password = getpass('Enter SSH Password: ')
    device = driver(address, username, password)
    print('Connecting to device...')
    device.open()
    return device

def find_mac(findme):
    return

def find_port(mac):
    return

def main():
    os.system('clear')
    args = get_args()
    driver = args.driver
    locate_ip = args.locate_ip
    start_ip = args.start_ip
    username = args.username
    verbosity = args.verbose

    device = init_device(start_ip, username)
    print('Retrieving ARP table...')
    arp_table = device.get_arp_table()
    for entry in arp_table:
        if locate_ip == entry['ip']:
            mac_addr = entry['mac']
            print(entry)
    print('Retrieving MAC address table...')
    mac_table = device.get_mac_address_table()
    for entry in mac_table:
        if mac_addr == entry['mac']:
            print(entry)
    device.close()
    return

if __name__ == '__main__':
    main()
