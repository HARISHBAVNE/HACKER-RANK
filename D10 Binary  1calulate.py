#input = 5 binary(101)
#output = 1
#input = 13 binary(1101)
#output = 2
#input = 6 binary(0110)
#output = 2

import math
import os
import random
import re
import sys

maxi = 0
icnt = 0
number = int(input())               # number from user
num = str(bin(number))              # convert number into binary and then into string 
for i in num:                       # loop to calculate consicutive one
    if i == "1":
        icnt += 1
    else:
        if maxi <= icnt:
            maxi = icnt
            icnt = 0
        else:
            icnt = 0
if (maxi < icnt):
    maxi = icnt
print(maxi)
