#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Week 7
'''

from snmp_helper import snmp_get_oid_v3, snmp_extract

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"

import pyeapi
from pprint import pprint

def main():

   # create the node instance
   node = pyeapi.connect_to('pynet-sw1')

   # go out and grab the "show interfaces" output
   show_int = node.enable('show interfaces')

   # Output from above returns a list; striping off list
   # leaving me a dictionary
   show_int = show_int[0]

   # I just want the output of the result key from the
   # dictionary above
   interfaces = show_int['result']

   interfaces = interfaces['interfaces']

   print "\n{:20} {:<20} {:<20}".format("Interface", "In Octets", "Out Octets")

   for i in interfaces.keys():
      int = interfaces.get(i)
      int_c = int.get('interfaceCounters')
      inOct = int_c.get('inOctets')
      ouOct = int_c.get('outOctets')
      print "{:20} {:<20} {:<20}".format(i, inOct, ouOct)

if __name__ == '__main__':
   main()

