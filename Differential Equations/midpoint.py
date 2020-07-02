import math

#enter your function here
def dydx(x, y):
    return (x * math.exp(3*x) - 2 * y)

def midpoint(x0, y0, x, h):
    n = (int)((x - x0)/h)
    y = y0 
    x = x0
    for i in range(0, n ):
        x = x0 + 0.5 * h 
        y1 = y + 0.5 * h * dydx(x0, y)
        y = y +  h * dydx(x, y1)
        x0 = x0 + h
        print("iteration ",i+1)
        print("x(",i+0.5,") = ",x,", x(",i+1,") = ",x0,", y(",i+0.5,")= ",round(y1,6),", y(",i+1,")= ",round(y,6))
        print(" ")

#Enter arguments
x0 = 0
y = 0
x = 1
h = 0.5
midpoint(x0, y, x, h)
