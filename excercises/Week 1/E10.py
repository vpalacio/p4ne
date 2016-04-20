#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 10
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

    crypto_g2 = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", 
                                               childspec=r"AES")

    for parent in crypto_g2:
      print parent.text
      for child in parent.children:
         print child.text

if __name__ == '__main__':
    main()
