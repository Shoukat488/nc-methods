import math

#enter your function here
def dydx(x, y):
    return ((x - y)/2)

def rungeKutta(x0, y0, x, h):
    n = (int)((x - x0)/h)
    y = y0 
    print("# \t\t k1 \t\t k2 \t\t k3 \t\t k4 \t\t x \t\t y")
    for i in range(1, n + 1):
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h 
        print(i,"\t   ",k1,"\t   ",k2,"\t   ",k3,"\t   ",k4,"\t   ",x0,"\t   ",y)
        print()
    return y


#Enter arguments
x0 = 0
y = 1
x = 2
h = 0.2
print('The value of y at x is:', rungeKutta(x0, y, x, h))
