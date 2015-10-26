import numpy
from cffi import FFI
 
ffi = FFI()

Ccode = open('C_fmandel.c', 'r').read()
ffi.set_source("_mandelbrot", Ccode) 

Cdefs = open('C_fmandel.h', 'r').read()
ffi.cdef(Cdefs)


if __name__ == "__main__":
    ffi.compile()
