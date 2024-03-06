"""
author: Alexey Aleshchenok
date: 2024-03-03
A program that sends empty TCP packets to the ports of a given IP address
and checks whether the port is open
"""
from scapy.all import *

TIMEOUT = 0.05


def check_port(remote_ip, port):
    """
    Send TCP packet to chosen port and check the received answer
    :param remote_ip: Host's IP
    :param port: Port
    :return: True if port is open, and False if it's not
    """
    response = sr1(IP(dst=remote_ip)/TCP(dport=port, flags="S"), timeout=TIMEOUT)
    if response is None or response[TCP].flags == "R":
        return False
    elif response[TCP].flags == "SA":
        return True
    else:
        return False


def main():
    """main function"""
    remote_ip = input('Enter the remote host address: ')
    open_ports = []
    for port in range(20, 1025):
        if check_port(remote_ip, port):
            print(f'Port {port} is open')
            open_ports.append(port)
        else:
            print(f'Port {port} closed')
    print(open_ports)


if __name__ == '__main__':
    main()
