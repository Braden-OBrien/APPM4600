import numpy as np
import matplotlib.pyplot as plt
import remez_poly as remez #credit to GitHub @DKenefake
import time

order = 3

f = lambda x: (np.e)**x

pts = np.linspace(-1, 1, 1000)

coeffs, err = remez.remez(f, order, -1, 1)

def poly_generator(coeff, order):
    return lambda x: coeff * (x**order)

minimax_list = [(coeffs[index], index) for index in range(len(coeffs))]
minimax = lambda x: sum(poly_generator(coeff, order)(x) for coeff,order in minimax_list)

plt.plot(pts, f(pts))
plt.plot(pts, minimax(pts))
plt.legend(["e^x", "minimax"])
plt.savefig('remez_ex_plot')

print('generated remez approximation of order', order)
print('approximate maximum error of approximation:', err)

pts = (np.linspace(-np.pi, np.pi, 100000))

time_initial = time.perf_counter()
f(pts)
time_function = time.perf_counter()
minimax(pts)
time_minimax = time.perf_counter()

print('calc time for function:', time_function-time_initial)
print('calc time for minimax:', time_minimax-time_function)