#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 8
'''

import yaml
import json

from pprint import pprint

from ciscoconfparse import CiscoConfParse

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"


def main():

    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    print "Parsing ..."
    print cisco_cfg
    print 

    crypto_map_list = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    print "Finding crypto map entries..."
    for parent in crypto_map_list:
      print parent.text
      for child in parent.children:
      	print child.text

if __name__ == '__main__':
    main()
