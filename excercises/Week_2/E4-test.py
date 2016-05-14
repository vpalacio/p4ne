#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 4 - Create a script that connects to 
both routers (pynet-rtr1 and pynet-rtr2) and p
rints out both the MIB2 sysName and sysDescr.
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
        print '#'
        for snmp_oid in (sysDescr, sysName):
            snmp_data = snmp_get_oid(device, oid=snmp_oid, display_errors=True)
            output = snmp_extract(snmp_data)
            print output

'''
    # get snmp data for rtr1
    print '# RTR1'
    snmp_data1 = snmp_get_oid(a_device1, oid=sysDescr, display_errors=True)
    output_rtr1 = snmp_extract(snmp_data1)
    print output_rtr1

    snmp_data1 = snmp_get_oid(a_device1, oid=sysName, display_errors=True)
    output_rtr1 = snmp_extract(snmp_data1)
    print output_rtr1
    print '# RTR1'
    print

    # get snmp data for rtr2
    print '# RTR2'
    snmp_data2 = snmp_get_oid(a_device2, oid=sysDescr, display_errors=True)
    output_rtr2 = snmp_extract(snmp_data2)
    print output_rtr2

    snmp_data2 = snmp_get_oid(a_device2, oid=sysName, display_errors=True)
    output_rtr2 = snmp_extract(snmp_data2)
    print output_rtr2
    print '# RTR2'
    print
'''

if __name__ == '__main__':
    main()

