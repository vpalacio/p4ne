#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Week 3: Excercise 1 - Create a snmpv3 script that connects to 
both routers (pynet-rtr1 and pynet-rtr2)
'''

from snmp_helper import snmp_get_oid_v3, snmp_extract

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"


def main():

    IP = '50.76.53.27'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_port1 = 7961
    snmp_port2 = 8061
    snmp_user = (a_user, auth_key, encrypt_key)
    RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    SYS_NAME = '1.3.6.1.2.1.1.5.0'
    SYS_UPTIME = '1.3.6.1.2.1.1.3.0'
    pynet_rtr1 = (IP, snmp_port1)
    pynet_rtr2 = (IP, snmp_port2)

    snmp_data = snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=RUN_LAST_CHANGED)
    output = snmp_extract(snmp_data)
    print "RUN_LAST_CHANGED: ", output
    

    snmp_data = snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=SYS_UPTIME)
    output = snmp_extract(snmp_data)
    print "SYS_UPTIME: ",output


if __name__ == '__main__':
    main()

