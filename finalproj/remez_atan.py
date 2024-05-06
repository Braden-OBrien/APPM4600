import numpy as np
import mpmath
import matplotlib.pyplot as plt
import remez_poly as remez #credit to GitHub @DKenefake
import time

order = 7

#f = lambda x: (np.e)**x
f = lambda x: mpmath.atan(x)

pts = np.linspace(-np.pi, np.pi, 1000)

coeffs, err = remez.remez(f, order, -np.pi, np.pi)

def poly_generator(coeff, order):
    return lambda x: coeff * (x**order)

minimax_list = [(coeffs[index], index) for index in range(len(coeffs))]
minimax = lambda x: sum(poly_generator(coeff, order)(x) for coeff,order in minimax_list)

res = [f(pt) for pt in pts]

plt.plot(pts, res)
plt.plot(pts, minimax(pts))
plt.legend(["atan(x)", "minimax approx"])
plt.savefig('remez_ex_plot')

print('generated remez approximation of order', order)
print('approximate maximum error of approximation:', err)

N = [100, 1000, 10000, 100000, 1000000]
times = [np.zeros(2*len(N)) for i in range(10)]
print(times)

for i in range(10):
    for n in range(len(N)):
        print(N[n])

        pts = (np.linspace(-np.pi, np.pi, N[n]))

        time_initial = time.perf_counter()
        [f(pt) for pt in pts]
        time_function = time.perf_counter()
        [minimax(pt) for pt in pts]
        time_minimax = time.perf_counter()

        times[i][n] = time_function-time_initial
        times[i][n+5] = time_minimax-time_function

for n in range(len(N)):
    avg_function = np.average([times[i][n] for i in range(10)])
    avg_minimax = np.average([times[i][n+5] for i in range(10)])
    
    print(N[n])
    print('calc time for function:', avg_function)
    print('calc time for minimax:', avg_minimax) 
