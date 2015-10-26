#include <stdlib.h>
 
float f(float x, float y, int max_iter)
{
  // r => real part
  // i => imaginary part
  
  float cr = x, ci = y, zr = 0, zi = 0;
  int n;

  
  for (n = 0; n < max_iter; n++)
  {
    float tzr = zr, tzi = zi;
    
    zr = tzr*tzr - tzi*tzi + cr;
    zi = 2*tzr*tzi + ci;
    
    if (zr*zr + zi*zi > 4.0)
    {
      break;
    }
  }
  
  return 1.0 - (float)n/(float)max_iter;
}
 
void mandelbrot(float x0, float y0, float x1, float y1, int grid, int max_iter, float* mv){
  float dx = (x1 - x0)/(float)grid, dy = (y1 - y0)/(float)grid;
  int n, m;
  
  for (n = 0; n < grid; n++)
  {
    for (m = 0; m < grid; m++)
    {
      mv[n * grid + m] = f(x0 + (float)m * dx, y0 + (float)n * dy, max_iter);
    }
  }
}
