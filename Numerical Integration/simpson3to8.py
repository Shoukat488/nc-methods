# Python code for simpson's 1 / 3 rule
import math
import numpy as np
# Function to calculate f(x)


def f(x):
    return ((2*x)/(x**2 - 4))
# Function for approximate integral


def simpson(a, b, n=3):
    h = (b-a)/n
    print("---------------Simpson 3/8 Rule ------------")
    print("")
    print("h=(b-a)/n =>")
    print("h=({:.3f} -{:.3f})/{:1}".format(b, a, n))
    print("")
    k = 0.0
    x = a + h
    i = 1
    print("f(x) = 3({:1.3f})/8[f({:1.3f})".format(h, a), end=" + ")
    while x <= (b-h):
        if i % 3 == 0:
            print("2f({:1.3f})".format(x), end=" + ")
        else:
            print("3f({:1.3f})".format(x), end=" + ")
        x += h
        i += 1
    print("f({:1.3f}) ]".format(b))
    print("")

    temp = 0
    x = a + h
    i = 1
    print("f(x) = 3({:1.3f})/8[{:1.3f}".format(h, f(a)), end=" + ")
    while x <= (b-h):
        if i % 3 == 0:
            temp = 2*f(x)
            print("{:1.3f}".format(temp), end=" + ")
            k += temp
        else:
            temp = 3*f(x)
            print("{:1.3f}".format(temp), end=" + ")
            k += temp
        x += h
        i += 1
    print("{:1.3f} ]".format(f(b)))
    print("")
    return (3*h/8)*(f(a)+f(b)+k)


# Driver code
a = 1  # Lower limit
b = 1.6  # Upper limit
n = 3  # Number of interval
print("f(x) = ", simpson(a, b))
