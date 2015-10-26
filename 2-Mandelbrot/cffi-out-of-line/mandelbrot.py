import numpy as np
import pylab as pl
from _mandelbrot import ffi, lib

def mandelbrot(x0=-2.0, y0=-1.5, x1=1.0, y1=1.5, grid=50, max_iter=1000):
  g = np.empty((grid, grid), dtype=np.float32)
  lib.mandelbrot(x0, y0, x1, y1, grid, max_iter, ffi.cast("float*", g.ctypes.data))
  return g

g = mandelbrot(grid=1000, max_iter=100)
pl.imshow(g, cmap=pl.cm.gray)
pl.show()
