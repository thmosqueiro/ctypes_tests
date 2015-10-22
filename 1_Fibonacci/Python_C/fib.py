import numpy as np
import ctypes

lib = ctypes.cdll['./FibonacciLib.so']
fib = lib['fib']

for j in range(15):
    x = 3*j + 3
    print "fib(%d) = %d" %( x,fib(x) )
