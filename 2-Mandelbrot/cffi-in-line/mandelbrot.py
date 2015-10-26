import numpy
from cffi import FFI
 
ffi = FFI()
ffi.cdef("""
float f(float, float, int);
void mandelbrot(float, float, float, float, int, int, float*);
""")
lib = ffi.verify("""#include <C_fmandel.h>""", include_dirs=['./'], sources=['C_fmandel.c'])
 
def mandelbrot(x0=-2.0, y0=-1.5, x1=1.0, y1=1.5, grid=50, max_iter=1000):
  g = numpy.empty((grid, grid), dtype=numpy.float32)
  lib.mandelbrot(x0, y0, x1, y1, grid, max_iter, ffi.cast("float*", g.ctypes.data))
  return g
 

import pylab
g = mandelbrot(grid=1000, max_iter=100)
pylab.imshow(g, cmap=pylab.cm.gray)
pylab.show()
