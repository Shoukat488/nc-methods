# Python code for simpson's 1 / 3 rule 
import math
import numpy as np
# Function to calculate f(x) 
def f( x ): 
	return  (1 / (x*np.log(x)))  
# Function for approximate integral 
def simpson( a, b, n):
    h=(b-a)/n
    print("---------------Simpson 1/3 Rule ------------")
    print("")
    print("h=(b-a)/n =>")
    print("h=({:.3f} -{:.3f})/{:1}".format(b,a,n))
    print("")
    k=0.0
    x=a + h
    print("f(x) = {:1}/3[f({:1})".format(h,a),end=" + ")
    for i in range(1, n):
        if i % 2 != 0:
            print("4f({:1})".format(x),end=" + ")
        else:
            print("2f({:1})".format(x),end=" + ")
        x += h
    print("f({:1}) ]".format(b))
    print("")

    temp = 0
    x = a + h
    print("f(x) = {:1}/3[{:1}".format(h,f(a)),end=" + ")
    for i in range(1, n):
        if i % 2 != 0:
            temp = 4*f(x)
            print("{:1}".format(temp),end=" + ")
            k += temp
        else:
            temp = 2*f(x)
            print("{:1}".format(temp),end=" + ")
            k += temp
        x += h
    print("{:1} ]".format(f(b)))
    print("")

    return (h/3)*(f(a)+f(b)+k)
# Driver code 
lower_limit = np.e # Lower limit 
upper_limit = np.e + 1 # Upper limit 
n = 2 # Number of interval 
print("f(x) = ",simpson(lower_limit, upper_limit, n)) 
