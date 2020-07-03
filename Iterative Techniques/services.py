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
            print(A[i][j] ,end="\t")
        print("")
    print("")

def CheckCondition(A):
    flag = True
    for i in range(len(A)):
        print("|",A[i][i],"| > ", end=" ")
        sum = 0
        daignol = abs(A[i][i])
        for j in range(len(A)):
            if j != i:
                print(" + |",A[i][j],"|", end=" ")
                sum += abs(A[i][j])
        if sum > daignol:
            print(" condition false",)
            flag = False
        else:
            print(" condition true",)
    print("")
    return flag
