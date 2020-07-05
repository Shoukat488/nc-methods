import numpy


def Arrange(A):
    n = len(A)
    flag = False
    for x in range(0, n-1):
        for i in range(n-1):
            for j in range(0, n-i-1):
                if A[j][x] < A[j+1][x]:
                    flag = True
                    for k in range(0, n):
                        A[j][k], A[j+1][k] = A[j+1][k], A[j][k]

        if flag == True:
            return A
    return A


def PrintArray(A):
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            print("{:10}".format(round(A[i][j],3)), end="\t")
        print("")
    print("")


def CheckCondition(A):
    flag = True
    for i in range(len(A)):
        print("|{:2} | > ".format(A[i][i]), end=" ")
        sum = 0
        daignol = abs(A[i][i])
        for j in range(len(A)):
            if j != i:
                print(" + | {:2}  |".format(A[i][j]), end=" ")
                sum += abs(A[i][j])
        if sum > daignol:
            print(" condition false",)
            flag = False
        else:
            print(" condition true",)
    print("")
    return flag


def isEqual(A, B):
    n1 = len(A)
    n2 = len(B)
    n = n1
    if n1 != n2:
        return False
    for i in range(0, n):
        for j in range(0, n):
            if A[i][j] != B[i][j]:
                return False
    return True


def solveDecompositon(L, U, b, option):
    y = numpy.linalg.solve(L, b)
    print("Solving LY = b:")
    print("Y =>")
    for i in range(0, len(y)):
        print("{:12}".format(round(y[i], 3)))
    print("")
    if option == 'b':
        print("Solving LtX = Y:")
    # elif option == 'c':
        # print()
    else:
        print("Solving UX = Y:")
    x = numpy.linalg.solve(U, y)
    print("X (Final solution) =>")
    for i in range(0, len(x)):
        print("{:12}".format(round(x[i], 3)))
    print("")


def Multiplication(A, B):
    return numpy.dot(A, B)


def solveLDLt(L, D, Lt, b):
    z = numpy.linalg.solve(L, b)
    print("Solving LZ = b:")
    print("Z =>")
    for i in range(0, len(z)):
        print("{:12}".format(round(z[i], 3)))
    print("")
    y = numpy.linalg.solve(D, z)
    print("Solving DY = Z:")
    print("Y =>")
    for i in range(0, len(y)):
        print("{:12}".format(round(y[i], 3)))
    print("")
    print("Solving LtX = Y:")
    x = numpy.linalg.solve(Lt, y)
    print("X (Final solution) =>")
    for i in range(0, len(x)):
        print("{:12}".format(round(x[i], 3)))
    print("")
