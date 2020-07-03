from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
import os;
os.system('cls')
def jacobi(A,b,N=25,x=None):
    #Solves the equation Ax=b via the Jacobi iterative method.
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - dot(R,x)) / D
        print("Iteratin: ",i+1)
        print("x :")
        print(x)
    return x

A = array([[3,-1,1],[3,6,2],[3,3,7]])
b = array([1.0, 0.0, 4.0])

# N is no of iterations
sol = jacobi(A,b,N=2)
