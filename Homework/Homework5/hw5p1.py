import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

def barylagrange(f, x, w, z):
    p = []
    num, denom = 0, 0
    for j in range(len(z)):
        for i in range(len(x)):
            if (z[j] != x[i]):
                num += (w[i]/(z[j]-x[i]))*f(x[i])
                denom += (w[i]/(z[j]-x[i]))
        p.append(num/denom)
        num, denom = 0, 0    
    return p

def calc_psi(z, x):
    p = []
    prod = 1
    for j in range(len(z)):
        for i in range(len(x)):
            if (z[j] != x[i]):
                prod *= np.abs(z[j]-x[i])
        p.append(prod)
        prod = 1
    return p

N = 16

h = 2/N

"""Equispaced nodes"""
x = np.zeros(N+1)
w = np.ones(N+1)
for i in range(N+1):
    x[i] = -1 + ((i+1)-1)*h

"""Chebyshev nodes"""
#x = np.zeros(N)
#w = np.ones(N)
#for i in range(N):
#    x[i] = np.cos(((2*i+1)*np.pi)/(2*(N+1)))


f = lambda x: 1/(1+(16*x)**2)

dat = f(x)

y = np.linspace(-1, 1, 1001)

p = interp.barycentric_interpolate(x, dat, y)

barylagrange(f, x, w, y)

plt.plot(x, f(x), 'o')
plt.plot(y, f(y))
plt.plot(y, p)

plt.savefig('fig')

plt.clf()

dat = np.log10(calc_psi(y, x))

plt.plot(y, dat)
plt.savefig('aaa')