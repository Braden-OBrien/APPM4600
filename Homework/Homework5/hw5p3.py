import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate._cubic as cubic

f = lambda x: np.sin(9*x)

N = 40*np.pi

x = np.arange(0, np.pi, np.pi/N)
y = f(x)
y[len(y)-1] = 0


interp = cubic.CubicSpline(x, y, bc_type="periodic")

z = np.linspace(0, 1, 1000)
real = f(z)
approx = interp(z)

dat = np.log(np.abs(real-approx))

plt.plot(z, dat)
plt.savefig('hw5p3')