from cffi import FFI
ffi = FFI()

ffi.cdef("int fib(int *);")
Ccode = open('Fibonacci.c')
ffi.set_source("_fibLib",
               """
               #include <stdio.h>
               
               int fib(int x)
               {
               if (x <= 1)
               return 1;
               else
               return fib(x-1) + fib(x-2);
               }
               """
)

if __name__ == "__main__":
    ffi.compile()
