# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import os
import sys

print(sys.path)
help("modules")

# These are things we will use later!
days_of_the_week = 7
def say_hello(recipient):
    print("Hello, world! Hello {}".format(recipient))
    return recipient