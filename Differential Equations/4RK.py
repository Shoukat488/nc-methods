import math

#enter your function here
def dydx(x, y):
    return (x * math.exp(3*x) - 2 * y)

def rungeKutta(x0, y0, x, h):
    n = (int)((x - x0)/h)
    y = y0 
    for i in range(1, n + 1):
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h 
        print("i= ",i," k1= ",round(k1,6)," k2= ",round(k2,6)," k3= ",round(k3,6)," k4= ",round(k4,6)," x0= ",round(x0,6)," y= ",round(y,6))
    return y

#Enter arguments
x0 = 0
y = 0
x = 1
h = 0.5
print('The value of y at x is:', round(rungeKutta(x0, y, x, h),6))
