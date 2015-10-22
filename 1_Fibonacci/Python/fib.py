def fib(x):
    if x <= 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


for j in range(15):
    x = 3*j + 3
    print "fib(%d) = %d" %( x,fib(x) )
