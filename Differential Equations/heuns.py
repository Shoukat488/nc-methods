import math
import numpy as np

# enter your exact function here
def exact(x, y):
    return x * np.log(x) + 2 * x


# enter your corrector functions here
def dydx(x, y):
    return 1 + y / x


def Heuns(x0, y0, x, h):
    n = (int)((x - x0) / h)
    x = x0
    yc = y0
    for i in range(0, n):
        yp = yc + h * dydx(x, yc)
        d1 = dydx(x, yc)
        x = x + h
        d2 = dydx(x, yp)
        yc = yc + 0.5 * h * (d1 + d2)
        print("iteration ", i + 1)
        print("x(", i + 1, ") = ", x, " yp= ", round(yp, 6), ", yc= ", round(yc, 6))
        ye = exact(x, yc)
        error = ((ye - yc) / ye) * 100
        print("Error = ",round(error,6),"%" )  
        print(" ")


# Enter arguments
x0 = 1
y = 2
x = 2
h = 0.25
Heuns(x0, y, x, h)
