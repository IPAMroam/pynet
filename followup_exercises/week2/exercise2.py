#!/usr/bin/env python
"""Idempotent configuration of VLAN IDs and names using Netmiko."""
import re
import threading
from Queue import Queue
from netmiko import ConnectHandler
from my_devices import device_list

def check_vlan_exists(output):
    """
    Check whether VLAN id exists in the VLAN database.

    801   blue                             active

    % VLAN 801 not found in current VLAN database
    """
    pattern = r"%.*not found in current VLAN database"
    return not bool(re.search(pattern, output))

def check_vlan_name(output, vlan_name):
    """
    Check VLAN name
    801   blue                             active
    """
    return vlan_name in output

def add_vlan(net_connect, vlan_id, vlan_name=''):
    """Use Netmiko to add VLAN name and ID."""
    cmd1 = "vlan " + str(vlan_id)
    cmds = [cmd1,]
    if vlan_name:
        cmd2 = "name " + vlan_name
        cmds.append(cmd2)
    return net_connect.send_config_set(cmds)

def ssh_conn(a_device, my_queue):
    """Handle SSH connection and passing data back to main thread."""
    new_vlans = [
        ('801', 'blue'),
        ('802', 'red'),
        ('803', 'orange'),
    ]

    net_conn = ConnectHandler(**a_device)
    device_name = net_conn.base_prompt
    output_dict = {device_name: {}}

    for vlan_id, vlan_name in new_vlans:
        cmd = "show vlan id {}".format(vlan_id)
        output = net_conn.send_command(cmd)
        vlan_exists = check_vlan_exists(output)
        vlan_name_correct = check_vlan_name(output, vlan_name)
        if not vlan_exists or not vlan_name_correct:
            output = add_vlan(net_conn, vlan_id, vlan_name)
            output_dict[device_name][vlan_id] = 'changed'
        else:
            output_dict[device_name][vlan_id] = 'unchanged'

    my_queue.put(output_dict)


def main():
    """Idempotent configuration of VLAN IDs and names using Netmiko."""
    my_queue = Queue()

    for a_device in device_list:
        my_thread = threading.Thread(target=ssh_conn, args=(a_device, my_queue))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

    while not my_queue.empty():
        print my_queue.get()

if __name__ == "__main__":
    main()
