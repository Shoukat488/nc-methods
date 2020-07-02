import math

#enter your function here
def dydx(x, y):
    return (( 1 + 4*x ) * y ** 0.5)

def rungeKutta(x0, y0, x, h):
    n = (int)((x - x0)/h)
    y = y0 
    for i in range(1, n + 1):
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1 * h)
        k3 = h * dydx(x0 + h, y - k1 * h + 2 * k2 * h)
        y = y + (1.0 / 6.0)*(k1 + 4 * k2 + k3 )
        x0 = x0 + h 
        print('i= ',i," k1= ",round(k1,6)," k2= ",round(k2,6)," k3= ",round(k3,6)," x0= ",round(x0,6)," y= ",round(y,6))
    return y

#Enter arguments
x0 = 0
y = 1
x = 1
h = 0.25
print('The value of y at x is:', round(rungeKutta(x0, y, x, h),6))
