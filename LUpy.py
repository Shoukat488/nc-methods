import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [3, 1, 0], [2, 4, 1], [0, 2, 5]])
P, L, U = scipy.linalg.lu(A)


print ("P:")
pprint.pprint(P)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)