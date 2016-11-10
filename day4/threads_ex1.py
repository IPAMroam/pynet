#!/usr/bin/env python
from netmiko import ConnectHandler
from net_system.models import NetworkDevice
import django
import threading
import Queue


def write_file(filename, output):
    with open(filename, "w") as f:
        f.write(output)

def remote_cmd(a_device, my_queue):
    output_dict = {}
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    if 'juniper' in a_device.device_type:
        output = remote_conn.send_command_expect("show config")
    else:
        output = remote_conn.send_command_expect("show run")
    output_dict[a_device.device_name] = output
    my_queue.put(output_dict)

def main():
    django.setup()
    my_queue = Queue.Queue()
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        my_thread = threading.Thread(target=remote_cmd, args=(a_device, my_queue))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

    while not my_queue.empty():
        my_dict = my_queue.get()
        for hostname, output in my_dict.items():
            filename = "{}.cfg".format(hostname)
            base_dir = '/home/kbyers/CFGS'
            full_file = "{}/{}".format(base_dir, filename)
            write_file(full_file, output) 

if __name__ == "__main__":
    main()
