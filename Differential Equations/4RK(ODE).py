import math
import numpy as np
#enter your function here
def dydx(x, y , z ):
    return (-2 * y + 5 * math.exp(-x))

def dzdx(x, y, z ):
    return (- ( y * (z ** 2))/2 )

def rungeKutta(x0, y0, z0,  x, h):
    n = (int)((x - x0)/h)
    y = y0
    z = z0
    for i in range(1, n + 1):
        k1 = h * dydx(x0, y, z)
        l1 = h * dzdx(x0,y,z)
        
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1, z + 0.5 * l1)
        l2 = h * dzdx(x0 + 0.5 * h, y + 0.5 * k1, z + 0.5 * l1)
        
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2, z + 0.5 *l2)
        l3 = h * dzdx(x0 + 0.5 * h, y + 0.5 * k2, z + 0.5 *l2)
        
        k4 = h * dydx(x0 + h, y + k3, z + l3)
        l4 = h * dzdx(x0 + h, y + k3, z + l3)
        
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        z = z + (1.0 / 6.0)*(l1 + 2 * l2 + 2 * l3 + l4)
        
        x0 = x0 + h 
        print("iteration ",i)
        print(" k1= ",round(k1,6)," k2= ",round(k2,6)," k3= ",round(k3,6)," k4= ",round(k4,6))
        print(" l1= ",round(l1,6)," l2= ",round(l2,6)," l3= ",round(l3,6)," l4= ",round(l4,6))
        print(" x0= ",round(x0,6), " y= ",round(y,6), " z= ",round(z,6))
        print(" ")
    
    print("Final value of y = ",round(y,6), " z= ",round(z,6) )

#Enter arguments
x0 = 0
y0 = 2
x = 0.4
h = 0.1
z = 4
rungeKutta(x0, y0,z, x, h)
