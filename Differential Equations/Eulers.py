# Python Code to find approximation 
# of a ordinary differential equation 
# using euler method. 

# Consider a differential equation 
# dy / dx =(x + y + xy) 
def func( x, y ): 
	return (x + y + x * y) 
	
# Function for euler formula 
def euler( x0, y, h, x ): 
	temp = -0

	# Iterating till the point at which we 
	# need approximation 
    print("# iterations \t\t x \t\t y")
	for(int i = 0 ; i < x ; i++) 
		temp = y 
		y = y + h * func(x0, y) 
		x0 = x0 + h
        print(i,"\t\t ",x0,"\t\t ",y)

	# Printing approximation 
	print("Approximate solution at x = ", x, " is ", "%.6f"% y) 
	
# Driver Code 
# Initial Values 
x0 = 0
y0 = 1
h = 0.025

# Value of x at which we need approximation 
x = 0.1

euler(x0, y0, h, x) 
