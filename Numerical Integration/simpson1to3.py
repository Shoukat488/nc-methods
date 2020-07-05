# Python code for simpson's 1 / 3 rule 
import math
import numpy as np
import sympy as sy
import scipy.integrate as integrate
# Function to calculate f(x) 
def f( x ): 
	return  (1 + np.exp(-x)* np.sin(4*x))
# Function for approximate integral

# def simpson1to3Error(a, b):
#     x = sy.symbols('x')
#     y = (x**2)*(sy.exp(-x))  
#     d1 = sy.Derivative(y)
#     d1 = d1.doit()
#     print(d1)
    # y1 = y.diff(x)
    # y2 = y1.diff(x)
    # y3 = y2.diff(x)
    # print(y1)
    # i = y3()
def simpson( a, b, n = 2):
    h=(b-a)/n
    print("---------------Simpson 1/3 Rule ------------")
    print("")
    print("h=(b-a)/n =>")
    print("h=({:.3f} -{:.3f})/{:1}".format(b,a,n))
    print("")
    k=0.0
    x = a + h
    i = 1
    print("f(x) = {:1}/3[f({:1})".format(h,a),end=" + ")
    while  x <= (b - h):
        if i % 2 != 0:
            print("4f({:1})".format(x),end=" + ")
        else:
            print("2f({:1})".format(x),end=" + ")
        x += h
        i += 1;
    print("f({:1}) ]".format(b))
    print("")

    temp = 0
    x = a + h
    i = 1
    print("f(x) = {:1}/3[{:1}".format(h,f(a)),end=" + ")
    while  x <= (b - h):
        if i % 2 != 0:
            temp = 4*f(x)
            print("{:1}".format(temp),end=" + ")
            k += temp
        else:
            temp = 2*f(x)
            print("{:1}".format(temp),end=" + ")
            k += temp
        x += h
        i += 1;
    print("{:1} ]".format(f(b)))
    print("")

    return (h/3)*(f(a)+f(b)+k)
# Driver code 
a = 0 # Lower limit 
b = 1 # Upper limit 
n = 2 # Number of interval 
print("f(x) = ",simpson(a, b)) 

# simpson1to3Error(a, b)
