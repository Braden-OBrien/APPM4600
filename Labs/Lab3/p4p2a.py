from bisection_example import *
import numpy as np


f = lambda x: (x-1)*(x-3)*(x-5)
a = 0
b = 2.4
tol = 10**-5
Nmax = 100

[out, err] = bisection(f,a,b,tol,Nmax)

print('approx root is ' + str(out) + ' error message is ' + str(err))
