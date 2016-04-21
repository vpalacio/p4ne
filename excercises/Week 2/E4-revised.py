#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 4
'''

from snmp_helper import snmp_get_oid, snmp_extract

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"


def main():

    # My Variables
    # a_device is a tuple = (a_host, community_string, snmp_port)
    a_host = '50.76.53.27'
    comm_string = 'galileo'
    snmp_port1 = 7961
    snmp_port2 = 8061
    sysDescr = '.1.3.6.1.2.1.1.1.0'
    sysName = '.1.3.6.1.2.1.1.5.0'
    a_device1 = (a_host, comm_string, snmp_port1)
    a_device2 = (a_host, comm_string, snmp_port2)

    for device in (a_device1, a_device2):
        for snmp_oid in (sysDescr, sysName):
            snmp_data = snmp_get_oid(device, oid=snmp_oid, display_errors=True)
            output = snmp_extract(snmp_data)
            print output

if __name__ == '__main__':
    main()
