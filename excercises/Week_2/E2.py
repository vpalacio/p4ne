#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 2A
'''
import telnetlib
import time

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def main():

	# My Variables
	ip_addr = '50.76.53.27'
	username = 'pyclass'
	password = '88newclass'
	command1 = 'terminal length 0'
	command2 = 'show ip int brief'
	
	# Set up the telnet connection
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
	print output

	# Submit username
    remote_conn.write( username + '\n')
	output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
	print output
    
	# submit password
    remote_conn.write( password + '\n')
    time.sleep(1)
	output = remote_conn.read_very_eager()
	print output

	# Submit 'term len 0'
    remote_conn.write ( command1 + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

	# Submit 'show ip int brief'
    remote_conn.write ( command2 + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    # Close the connection
	remote_conn.close()

if __name__ == '__main__':
    main()
