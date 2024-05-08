import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import remez_implementation
import remez_poly
import time

#input_function = lambda x: (np.e)**x
input_function = lambda x: np.arctan(x)
func2 = lambda x: mp.atan(x)
lower_bound = -1
upper_bound = 1
degree = 12

times_us = []
times_dk = []

errs = []

for i in range(1):
    time_us = time.perf_counter()
    (minimax, residual, err1, x_points) = remez_implementation.remez_polynomial(input_function, lower_bound, upper_bound, degree, ret_interp_nodes=1)#, saveplots=1, saveextremaplots=1, savelogplots=1)
    time_mid = time.perf_counter()
    res, err2 = remez_poly.remez(func2, degree, lower_bound, upper_bound)
    time_final = time.perf_counter()
    
    times_us.append(time_mid-time_us)
    times_dk.append(time_final-time_mid)
    errs.append((err1, err2))

print('degree is:', degree)

print('CPU Time for our implementation', np.average(times_us))
print('CPU Time for packaged implementation', np.average(times_dk))

print('Our err estimate is', err1)
print('Packaged err estimate is', err2)


points = np.linspace(-1, 1, 1000)

plt.plot(points, minimax(points))
plt.plot(points, input_function(points))
plt.scatter(x_points, [minimax(pt) for pt in x_points])
plt.savefig('remez_example_new')