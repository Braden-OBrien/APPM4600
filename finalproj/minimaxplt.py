import numpy as np
import matplotlib.pyplot as plt

f = lambda x: (np.e)**x

q = lambda x: (np.e - np.sinh(1)*np.log(np.sinh(1)))*(1/2) + np.sinh(1)*x

pts = np.linspace(-1, 1, 1000)

f_pts = f(pts)
q_pts = q(pts)

E_pts = f_pts - q_pts

plt.plot(pts, f(pts))
plt.plot(pts, q(pts))
plt.plot(pts, E_pts)
plt.legend(['f(x)', 'q(x)', 'E(x)'])
plt.savefig('plot')