import numpy as np
import pylab as pl

def f(x, y, max_iter=1000):
    
    c = x + y*1j
    z = (0 + 0j)
    
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return 1.0 - float(n)/max_iter

    return 0.0


def mandelbrot(x0=-2.0, y0=-1.5, x1=1.0, y1=1.5, grid=50, max_iter=1000):
    
    dx = float(x1 - x0)/grid
    dy = float(y1 - y0)/grid
    
    return [[ f(x0 + n*dx, y0 + m*dy, max_iter) for n in range(grid)]
            for m in range(grid)]


g = mandelbrot(grid=1000, max_iter=100)
pl.imshow(g, cmap=pl.cm.gray)
pl.show()
