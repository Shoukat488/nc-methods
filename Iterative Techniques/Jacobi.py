from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot, array_equal, round
import services as Services


def jacobi(A, b, N=25, x=None):
    # Solves the equation Ax=b via the Jacobi iterative method.
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R, x)) / D
        print("Iteratin: ", i+1)
        for k in range(0, len(x)):
            print("x(", k+1, ") = ", round(x[k], 6), end=", ")
        print("\n")

    return x


A = [[2, -6, 8], [5, 4, -3], [3, 1, 2]]
b = array([24.0, 2.0, 16.0])

print("Equations given =>")
Services.PrintArray(A)
arranged = A
print("Checking Condition =>")
print("")
conditon = Services.CheckCondition(arranged)
if conditon == False:
    arranged = Services.Arrange(A)
    Services.PrintArray(arranged)
    # print(array_equal(arranged, A))
    print(arranged == A)
    
    if arranged == A:
        print("It isn't a diagnolly dominent, Therefore solution will be diverged")
        print("k")
    else:
        print("Rearranging equaitions =>")
        Services.PrintArray(arranged)
        print("Checking Condition Again =>")
        print("")
        conditon = Services.CheckCondition(arranged)
        if conditon == True:
            print("It's a diagnolly dominent, Therefore solution will be converged")
            print("")
        else:
            print("It isn't a diagnolly dominent, Therefore solution will be diverged")
            print("k")
else:
    print("It's a diagnolly dominent, Therefore solution will be converged")
    print("k")
# N is no of iterations

sol = jacobi(arranged, b, N=2)
