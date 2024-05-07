import numpy as np
import matplotlib.pyplot as plt
import remez_implementation

input_function = lambda x: (np.e)**x
lower_bound = -1
upper_bound = 1
degree = 3

(minimax, residual, err, x_points) = remez_implementation.remez_polynomial(input_function, lower_bound, upper_bound, degree, ret_interp_nodes=1)

points = np.linspace(-1, 1, 1000)

plt.plot(points, residual(points))
plt.scatter(x_points, [residual(pt) for pt in x_points])
plt.savefig('remez_example_new')