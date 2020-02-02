#!/bin/bash

import subprocess

#./doubt/somesh/python-testing-101/example-py-doctest/com/automationpanda/example/calc_func.py

cmd = 'python /doubt/somesh/python-testing-101/example-py-doctest/com/automationpanda/example/calc_func.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate() 
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)
