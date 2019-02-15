#!/usr/bin/python

import os
import sys


# Clear screen
clrscn = '\033c'
print(clrscn)

shorpy = input('''

    \033[01;33mWhat type of script do you want to create ?\033[01;37m

    \033[01;36m1\033[01;37m) \033[01;31mPYTHON

    \033[01;36m2\033[01;37m) \033[01;32mBASH



    \033[01;37m[\033[01;36m1\033[01;37m/\033[01;36m2\033[01;37m]: ''')

if shorpy == '1':
    filename = input('''

    Please enter filename: ''')
    filetomake = open(filename, "w")
    printtofile = filetomake.write('''#!/usr/bin/python

''')
    print(printtofile)
    filetomake.close() 
elif shorpy == "2":
    filename = input('''

    Please enter filename: ''')
    filetomake = open(filename, "w")
    printtofile = filetomake.write('''#!/bin/bash

''')
    print(printtofile)
    filetomake.close() 

os.system('nano +3,1 ' + filename)
