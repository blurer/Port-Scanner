# Port-Scanner
Python script for scanning tcp/udp port(s) on a given host

0_network.py - single ip/single port status
1_network.py - all open ports for a single ip

## Example: ./network.py

```
# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [23:05:53] 
$ ./0_network.py 

Simple TCP/IP Port Scanner

IPv4 Address: 10.1.1.1
TCP/UDP Port: 53


Port 53 Open

# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [23:06:00] 
$ ./0_network.py

Simple TCP/IP Port Scanner

IPv4 Address: 10.1.1.1
TCP/UDP Port: 443


Port 443 Closed

# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [23:07:05] 
$ ./0_network.py

Simple TCP/IP Port Scanner

IPv4 Address: 10.1.1.1
TCP/UDP Port: 8443


Port 8443 Open
```

## Example2: 1_network.py
```
# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [20:54:12]
$ ./1_network.py
------------------------------
TCP/IP Port Scanner
Shows open ports 1-65535
------------------------------
IPv4 Address: 10.1.1.7
------------------------------
Port 22 Open
Port 111 Open
Port 3128 Open
Port 8006 Open
------------------------------
```


## Planning to add:
* Network/Cidr mask
* More than single port
* IPv6

## Changelog:
* [9/17/18]: Added [port] to the output.
* [9/18/18]: Added 1_network.py:
