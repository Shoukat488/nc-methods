def Arrange(A):
    n = len(A)
    flag = False
    for x in range(0,n-1):
        for i in range(n-1):
            for j in range(0, n-i-1):
                if A[j][x] < A[j+1][x]:
                    flag = True
                    for k in range(0 , n):
                        A[j][k] , A[j+1][k] = A[j+1][k] , A[j][k]
                    
        if flag == True:
            return A
    return A

def PrintArray(A):
    n = len(A);
    for i in range(0 , n):
        for j in range(0 , n):
            print( "{:10}".format(A[i][j]) ,end="\t")
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

def isEqual(A,B):
    n1 = len(A)
    n2 = len(B)
    n = n1
    if n1 != n2:
        return False
    
    for i in range(0,n):
        for j in range(0, n):
            if A[i][j] != B[i][j]:
                return False
    return True

