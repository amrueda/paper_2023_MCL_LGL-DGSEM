#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:15:48 2023

@author: andresrueda
"""

import os
import sys
import numpy as np

def latex_float(f):
    if np.isnan(f):
        return "-"
    float_str = "{0:.2e}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        if int(exponent)==0:
            return r"{0}".format(base)    
        else:
            return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
        
    else:
        return float_str


# Read argument
n = len(sys.argv)
if n==2:
    file = sys.argv[1]
else:
    file = "log.txt"
        
# Read table
os.system("tail "+file+" -n 18 | head -n 5 > tmp.txt")

table = np.genfromtxt("tmp.txt", skip_header=0, names=True,invalid_raise=False)

# Print table
#print(" & ".join([table.dtype.descr[i][0] for i in range(len(table.dtype))])+" \\\\")

for line in range(table.size):
    print("$"+str(2**(line+2))+"$ & $"+"$ & $".join([latex_float(table[line][i]) for i in range(len(table.dtype))])+"$ \\\\")

# Remove auziliary files
os.system("rm tmp.txt")

