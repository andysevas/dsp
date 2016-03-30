# Matrix Algebra

import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.array([6, 2, -3 ,5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

#Matrix dimensions for part 1
print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print v.shape
print w.shape

#Vector operations for part 2
print u+v
print u-v
print 6*u
print u.dot(v)
print np.linalg.norm(v)

#Matrix operations for part 3
#3.1
try:
    print A + C
except ValueError:
    print "Not defined"

#3.2 - #3.4
print A - C.T
print C.T + 3*D
print B*A

#3.5
try:
    print B*(A.T)
except ValueError:
    print "Not defined"
