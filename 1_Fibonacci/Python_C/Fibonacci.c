#include <stdio.h>

int fib(int i)
{
    if (i<=1)
        return 1;
    else
        return fib(i-1)+fib(i-2);
}
