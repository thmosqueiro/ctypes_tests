#include <stdio.h>

int fib(int x) {
  if (x <= 1)
    return 1;
  else
    return fib(x-1) + fib(x-2);
}

int main(void) {
  
  int j,x;
  
  for (j=0; j < 15; j++) {
    x = j*3+3;
    printf( "fib(%d) = %d\n", x, fib(x) );
  }
  
  return 0;
}
