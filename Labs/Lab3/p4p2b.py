from bisection_example import *
import numpy as np


f = lambda x: ((x-1)**2)*(x-3)
a = 0
b = 2
tol = 10**-5
Nmax = 100

[out, err] = bisection(f,a,b,tol,Nmax)

print('approx root is ' + str(out) + ' error message is ' + str(err))
