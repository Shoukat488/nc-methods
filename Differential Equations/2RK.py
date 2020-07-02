import math;

def dydx(x, y):
    # print(x,y)
    return (( 1 + 4*x ) * y ** 0.5)
def rungeKutta(x0, y0, x, h):
    n = round((x - x0) / h)
    y = y0
    print("# \t\t\t k1 \t\t\t k2 \t\t\t x \t\t\t y")
    
    for i in range(1, n + 1):
        # print(i,"\t\t",k1,"\t\t",k2,"\t\t",x0,"\t\t",y);
        # print(dydx(x0, y))
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + h, y +  h * k1)
        y = y + 0.5 * (k1 + k2)
        x0 = x0 + h
        print(i,"\t\t   ",round(k1,6),"\t\t   ",round(k2,6),"\t\t   ",round(x0,6),"\t\t   ",round(y,6))
    return y;

if __name__ == "__main__": 
    x0 = 0; y = 1;
    x = 1; h = 0.25; 
    print("y(x) =",round(rungeKutta(x0, y, x, h),6)); 

# This code is contributed by Yash_R 
