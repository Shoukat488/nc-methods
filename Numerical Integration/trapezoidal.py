# Python code for simpson's 1 / 3 rule
import math
import numpy as np
# Function to calculate f(x)


def f(x):
    return (1 + np.exp(-x)* np.sin(4*x))
# Function for approximate integral


def trapezoidal(a, b, n=1):
    h = (b-a)/n
    print("---------------Simpson 3/8 Rule ------------")
    print("")
    print("h=(b-a)/n =>")
    print("h=({:.3f} -{:.3f})/{:1}".format(b, a, n))
    print("")
    k = 0.0
    x = a + h
    print("f(x) = ({:1.3f})/2[f({:1.3f})".format(h, a), end=" + ")
    while x <= (b-h):
        print("2f({:1.3f})".format(x), end=" + ")
        x += h
    print("f({:1.3f}) ]".format(b))
    print("")

    temp = 0
    x = a + h
    print("f(x) = ({:1.3f})/2[{:1.3f}".format(h, f(a)), end=" + ")
    while x <= (b-h):
        temp = 2*f(x)
        print("{:1.3f}".format(temp), end=" + ")
        k += temp
        x += h
    print("{:1.3f} ]".format(f(b)))
    print("")
    return (h/2)*(f(a)+f(b)+k)


# Driver code
a = 0  # Lower limit
b = 0.5  # Upper limit
n = 1  # Number of interval
print("f(x) = ", trapezoidal(a, b))
