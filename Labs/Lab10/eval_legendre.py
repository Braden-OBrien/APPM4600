import numpy as np

n = 5

x = 1

def eval_legendre(n, x):
    p = np.zeros(n+1)
    p[0] = 1
    p[1] = x

    it = 2

    while (it<=n):
        p[it] = (1/(n+1))*((2*n+1)*x*p[it-1] - n*p[it-2])
        it+=1

    return p


print(eval_legendre(n, x))

