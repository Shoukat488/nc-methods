import numpy as np
import scipy.linalg as la
import sys
sys.path.append("../")
import services as Services

option = input("Do you want to find solution also? y or n : ")

A = np.array([[4,-1,1],[-1,4.25,2.75],[1,2.75,3.5]])
b = np.array([1,0,0])

print("Given Matrix=>")
Services.PrintArray(A)

L , D ,  P = la.ldl(A)
Lt = np.transpose(L)
print("L:")
Services.PrintArray(L)
print("D:")
Services.PrintArray(D)
print("Lt:")
Services.PrintArray(Lt)

if option.lower() == 'y':
    Services.solveLDLt(L,D,Lt,b)