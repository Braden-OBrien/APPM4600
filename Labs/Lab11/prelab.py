import numpy as np

def trapezoidal(a, b, f, N):
    
    h = (b - a)/(N+1)
    
    dat = []
    dat.append(f(a))
    
    iter = a
    for i in range(N):
        iter+=h
        dat.append(2*f(iter))
    
    dat.append(f(b))
    
    ret = (h/2) * sum(dat)
    
    return ret

f = lambda x: (np.e)**x

a, b = 0, 4

N = 0

print(trapezoidal(a, b, f, N))