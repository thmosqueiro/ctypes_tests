from _fibLib import ffi, lib

buffer_in = ffi.new("int[]", 1000)
buffer_out = ffi.new("int[]", 1000)

result = lib.fib(6)
