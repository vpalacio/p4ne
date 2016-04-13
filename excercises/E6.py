#!/usr/bin/env python

'''
Python for Network Engineers: P4NE - Bring it!

Excercise 6
'''

import yaml
import json

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"


def main():

    my_dict = {
      'Course': 'P4NE',
      'Instructor': 'Kirk Byers',
      'Student': 'Victor Palacio',
      'Month': 'April',
      'Year': '2016',
      'Motto': 'Bring the P4NE!'
    }

    my_list = [
      'Python for Network Engineers',
      my_dict,
      'Excited',
      'Yeah!'
    ]

    with open("E6.yml", "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open("E6.json", "w") as f:
        json.dump(my_list, f)

if __name__ == '__main__':
    main()
