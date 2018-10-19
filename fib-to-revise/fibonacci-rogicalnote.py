# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:57:19 2018

@author: Takuto
"""
import sys
sys.setrecursionlimit(10000)

def fib(n):
    a,b=0,1
    if n>=2:
        return fib(n-1) + fib(n-2)
    elif n==0:
        return a
    else:
        return b

print(fib(2018))


print(fib(5))
