# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix
from numpy import array_equal, round , copy
import services as Services


def seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if(j != i):
                d -= a[j][i] * x[i]
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x


# int(input())input as number of variable to be solved
n = 3  # size of the row and column
iterations = 3
# initial solution depending on n(here n=3)
x = [0, 0, 0]
A = [[8, 2, -2], [1, -8, 3], [2, 1, 9]]
b = [8, -4, 12]

print("Equations given =>")
Services.PrintArray(A)
print("Checking Condition =>")
print("")
arranged = copy(A)

conditon = Services.CheckCondition(A)
if conditon == False:
    arranged = Services.Arrange(arranged)

    if Services.isEqual(A, arranged):
        print("It isn't a diagnolly dominent, Therefore solution will be diverged")
        print("")
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
    print("")
# loop run for m times depending on m the error value

for i in range(0, iterations):
    x = seidel(arranged, x, b)
    # print each time the updated solution
    print("iteration: ", i+1)
    for k in range(0, len(x)):
        print("x(", k+1, ") = ", round(x[k], 6), end=", ")
    print("\n")
