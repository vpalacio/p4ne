#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 6
'''

import yaml
import json

from pprint import pprint

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"

yml_file = 'E6.yml'
json_file = 'E6.json'


def main():

    with open(yml_file) as f:
        new_yml = yaml.load(f)

    with open(json_file) as f:
        new_json = json.load(f)

    pprint(new_yml)

    pprint(new_json)

if __name__ == '__main__':
    main()
