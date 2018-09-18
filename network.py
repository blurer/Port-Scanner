#!/usr/bin/python3

import sys
import socket
import ipaddress
import subprocess

ipAddress = input("IP Address? ")
port = int(input("Port Number? "))

str(ipAddress)

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipAddress, port))
    if result == 0:
        print("Port Open")
        break
    elif result != 0:
        print("Port Closed")
        break


