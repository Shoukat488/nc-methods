# Python code for simpson's 1 / 3 rule 
import math
import numpy as np
# Function to calculate f(x) 
def f( x ): 
	return  ((x**2)*np.power(np.exp(x),-x))  
# Function for approximate integral 
def simpson( a, b, n):
    h=(b-a)/n
    print("---------------Simpson 3/8 Rule ------------")
    print("")
    print("h=(b-a)/n =>")
    print("h=({:.3f} -{:.3f})/{:1}".format(b,a,n))
    print("")
    k=0.0
    x=a + h
    print("f(x) = 3({:1.3f})/8[f({:1.3f})".format(h,a),end=" + ")
    for i in range(1, n):
        if i % 3 == 0:
            print("2f({:1.3f})".format(x),end=" + ")
        else:
            print("3f({:1.3f})".format(x),end=" + ")
        x += h
    print("f({:1.3f}) ]".format(b))
    print("")

    temp = 0
    x = a + h
    print("f(x) = 3({:1.3f})/8[{:1.3f}".format(h,f(a)),end=" + ")
    for i in range(1, n):
        if i % 3 == 0:
            temp = 2*f(x)
            print("{:1.3f}".format(temp),end=" + ")
            k += temp
        else:
            temp = 3*f(x)
            print("{:1.3f}".format(temp),end=" + ")
            k += temp
        x += h
    print("{:1.3f} ]".format(f(b)))
    print("")
    return (3*h/8)*(f(a)+f(b)+k)
# Driver code 
a = 0 # Lower limit 
b = 1 # Upper limit 
n = 3 # Number of interval 
print("f(x) = ",simpson(a, b, n)) 

