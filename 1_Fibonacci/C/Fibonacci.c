#include <stdio.h>

int fib(int i) {
  if (i<=1)
    return 1;
  else
    return fib(i-1)+fib(i-2);
}

int main(void) {
  
  int j,x;
  
  for (j=0; j < 15; j++) {
    x = j*3+3;
    printf( "fib(%d) = %d\n", x, fib(x) );
  }
  
  return 0;
}
