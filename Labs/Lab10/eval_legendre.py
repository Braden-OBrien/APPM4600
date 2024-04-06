import numpy as np
import scipy.special

n = 5

x = 287

def eval_legendre(n, x):
    p = np.zeros(n+1)
    p[0] = 1
    p[1] = x

    it = 2

    while (it<=n):
        p[it] = (1/(n))*((2*n-1)*x*p[it-1] - n*p[it-2])
        it+=1

    return p

def scipy_leg(n, x):
    p = np.zeros(n+1)
    for j in range(0, n+1):
        p[j] = scipy.special.eval_legendre(j, x)
    return p

print(eval_legendre(n, x))
print(scipy_leg(n, x))

