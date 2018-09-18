# Port-Scanner
Python script for scanning tcp/udp port(s) on a given host

Example:

```
# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [23:05:53] 
$ ./network.py 

Simple TCP/IP Port Scanner

IPv4 Address: 10.1.1.1
TCP/UDP Port: 53


Port 53 Open

# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [23:06:00] 
$ ./network.py

Simple TCP/IP Port Scanner

IPv4 Address: 10.1.1.1
TCP/UDP Port: 443


Port 443 Closed

# bl @ bl-arch in ~/projects/Port-Scanner on git:master x [23:07:05] 
$ ./network.py

Simple TCP/IP Port Scanner

IPv4 Address: 10.1.1.1
TCP/UDP Port: 8443


Port 8443 Open
```

Planning to add:
* Network/Cidr mask
* More than single port
* IPv6

Changelog:
* Added [port] to the output.
