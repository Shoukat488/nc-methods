from math import sqrt
from pprint import pprint
import numpy as np
import scipy.linalg as la
import sys
sys.path.append("../")
import services as Services

option = input("Do you want to find solution also? y or n : ")
A = np.array([[4,2,14],[2,17,-5],[14,-5,83]])
b = np.array([14,-101,155])
print("Given Matrix=>")
Services.PrintArray(A)
try:
    Lt = la.cholesky(A)
    L  = np.transpose(Lt)
except RuntimeError as identifier:
    print(identifier)
print ("L:")
for i in  range(0,len(L)):
    for j in range(0,len(L)):
        print("{:15.3f}".format(L[i][j]), end = " ")
    print("")
print ("Lt:")
for i in  range(0,len(Lt)):
    for j in range(
        0,len(Lt)):
        print("{:15.3f}".format(Lt[i][j]), end = " ")
    print("")

if option.lower() == "y":
    Services.solveDecompositon(L,Lt,b,'b')
