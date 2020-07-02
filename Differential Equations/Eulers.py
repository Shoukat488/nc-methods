import math

# Python Code to find approximation
# of a ordinary differential equation
# using euler method.

# Consider a differential equation
# dy / dx =(x + y + xy)
def func(x, y):
    return x * math.exp(3 * x - 2 * y)


# Function for euler formula
def euler(x0, y, h, x):
    temp = -0
    # Iterating till the point at which we
    # need approximation
    i = -1
    print("# \t\t x \t\t y ")
    while x0 < x:
        i = i + 1
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h
        print(i, "\t\t", x0, "\t\t", y)

    # Printing approximation
    print("Approximate solution at x = ", x, " is ", "%.6f" % y)

# Driver Code
# Initial Values
# x0 = input("Enter initial value: ")
# x = input("Enter maximum value of x: ")
x0 = 0
y0 = 0
h = 0.5
x = 1
# Value of x at which we need approximation
euler(x0, y0, h, x)
