def Arrange(A):
    n = len(A)
    x = 0
    flag = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j][x] < A[j+1][x]:
                flag = True
                A[j][x] , A[j+1][x] = A[j+1][x] , A[j][x]
