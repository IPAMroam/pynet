#!/usr/bin/env python
"""
Use Netmiko to configure the interface descriptions on a switch or a router. Try to use Python
data structures and loop techniques to simplify this process (i.e. to eliminate code duplication.
"""
from __future__ import unicode_literals
from __future__ import print_function

from getpass import getpass
from netmiko import ConnectHandler

ip_addr = raw_input("Enter IP Address: ")

device = {
    'device_type': 'cisco_ios',
    'ip': ip_addr,
    'username': 'pyclass',
    'password': getpass(),
}

intf_desc = {
    'FastEthernet0': '',
    'FastEthernet1': '',
    'FastEthernet2': '',
    'FastEthernet3': '',
    'FastEthernet4': "descr *** LAN connection (don't change) ***",
    'Vlan1': '',
}

net_connect = ConnectHandler(**device)
# Make sure in enable mode
net_connect.enable()
config_cmds = []
for intf, descr in intf_desc.items():
    config_cmds.append('interface {}'.format(intf))
    if not descr:
        config_cmds.append('descr *** intf {} ***'.format(intf))
    else:
        config_cmds.append(descr)

output = net_connect.send_config_set(config_cmds)
print(output)
