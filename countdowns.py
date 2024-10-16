import ctypes
import time


lib = ctypes.CDLL("./libcountdown.so")
lib.countdown.argtypes = [ctypes.c_int]
lib.countdown.restype = ctypes.c_int
ip = int(input("Enter an arbitary integer value to test the program = "))
st = time.time()
result1 = lib.countdown(ip // 2)
result2 = lib.countdown(ip // 2)
et = time.time()
print(f" Time of execution in C {et-st}")


def countdown(x):
    while x >= 0:
        x += -1
    return True


st1 = time.time()
x = countdown(ip / 2)
x = countdown(ip / 2)
et1 = time.time()


print(f" Time of execution in python {et1-st1}")

print(
    "This simple program helps to understand why compiling on a low level language like C improves the execution speed of python programs"
)
