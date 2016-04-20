#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 2A
'''
import telnetlib

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def main():

	ip_addr = '50.76.53.27'
	username = 'pyclass'
	password = '88newclass'
	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
	remote_conn = remote_conn.write( username + '\n')
	output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
	remote_conn = remote_conn.write( password + '\n')
	output = remote_conn.read_very_eager()
	print output
	remote_conn.close()

if __name__ == '__main__':
    main()
