#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:11:12 2019

@author: wassim
"""

from random import randint

import time

ntimes = int(input("How many times do you want to play? "))

success = 0

start_time = time.perf_counter()

for i in range(ntimes):
    i = randint(0, 12)
    j = randint(0, 12-i)
    k = randint(0, 12)
    l = randint(0, 12-k)
    if randint(0, 1):
        n = int(input("(" + str(i) + " - " + str(j) + ") * ("  + str(k) + " + " + str(l) + ") = "))
        if n == (i-j)*(k+l): success += 1
        while n != (i-j)*(k+l):
            n = int(input("WRONG! (" + str(i) + " - " + str(j) + ") * ("  + str(k) + " + " + str(l) + ") = "))
    else:
        n = int(input("(" + str(i) + " + " + str(j) + ") * ("  + str(k) + " - " + str(l) + ") = "))
        if n == (i+j)*(k-l): success += 1
        while n != (i+j)*(k-l):
            n = int(input("WRONG! (" + str(i) + " + " + str(j) + ") * ("  + str(k) + " - " + str(l) + ") = "))

elapsed_time = time.perf_counter() - start_time

print("\n")
print("> Score:", str(success/ntimes*100) + "%")
print("> Elapsed time:", round(elapsed_time, 2))
print("> Time per question:", round(elapsed_time/ntimes, 2))
