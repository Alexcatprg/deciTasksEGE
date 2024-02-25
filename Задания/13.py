from ipaddress import *
k = 0
net = ip_network('64.192.192.0/255.255.240.0')
for ip in net:
    if bin(int(ip)).count('1') % 2 == 0:
        k += 1
print(k)