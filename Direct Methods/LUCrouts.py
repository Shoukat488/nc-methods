# Python3 Program to decompose
# a matrix into lower and
# upper traingular matrix
import sys
sys.path.append('../') 
import services as Services
MAX = 100


def Crouts(mat, b, n, option):

    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):

        # Upper Triangular
        for k in range(i, n):
            if (i == k):
                upper[i][i] = 1
            else:
                # Summation of L(i, j) * U(j, k)
                sum = 0
                for j in range(i):
                    sum += (lower[i][j] * upper[j][k])
                # Evaluating U(i, k)
                upper[i][k] = mat[i][k] - sum

        # Lower Triangular
        for k in range(i, n):
            # Summation of L(k, j) * U(j, i)
            sum = 0
            for j in range(i):
                sum += (lower[k][j] * upper[j][i])

            # Evaluating L(k, i)
            lower[k][i] = int((mat[k][i] - sum) /
                              upper[i][i])

    # setw is for displaying nicely
    print("Lower Triangular matrix:")
    Services.PrintArray(lower)
    print("Upper Triangular matrix:")
    Services.PrintArray(upper)
    if option.lower() == 'y':
        Services.solveDecompositon(lower, upper, b,'a')


option = input("Do you want to find solution also? y or n : ")

# Driver code
mat = [[1, 2, 3],
       [2, -4, 6],
       [3, -9, -3]]
b = [5, 18, 6]
print("Given matrix=> ")
Services.PrintArray(mat)
Crouts(mat, b, len(mat), option)

# This code is contributed by mits
