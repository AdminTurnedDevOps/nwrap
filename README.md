# nwrap

<p align="center">
 <img src="images/logo.png?raw=true" alt="Logo" width="50%" height="50%" />
</p>

A wrapper around `nmap` that exposes three commands. One to scan a specific IP, one to scan a specific range, and one to scan open ports.

## How To Use

There are four commands available:
✅ `ipport` - Scan one IP address to see if a port of your choosing is exposed.
✅ `ipscan` - Scan one IP address to see hostname and if it's up 
✅ `scaniprange` - Scan an IP range to see hosts, hostnames, and if they are up. 
✅ `scaniprangeport` - Scan a specific port and IP range to see if the Port is open on any IP addresses 

You can use it by calling upon the `main.py`. For example:

```
python3 nwrap/main.py ipport 22 192.168.1.249
```

```
python3 nwrap/main.py ipscan 192.168.1.249
```