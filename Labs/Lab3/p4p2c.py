from bisection_example import *
import numpy as np


f = lambda x: np.sin(x)
a = 0
b = 0.1
tol = 10**-5
Nmax = 100

[out, err] = bisection(f,a,b,tol,Nmax)

print('approx root for [0, 0.1] is ' + str(out) + ' error message is ' + str(err))

a = 0.5
b = np.pi * 3 / 4

[out, err] = bisection(f,a,b,tol,Nmax)

print('approx root for [0.5, 3pi/4] is ' + str(out) + ' error message is ' + str(err))
