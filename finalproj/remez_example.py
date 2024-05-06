import numpy
import mpmath as mp
import scipy
import matplotlib.pyplot as plt
import scipy.optimize

def chev_points(n:int, lower:float = -1, upper:float = 1):
    """
    Generates a set of chebychev points spaced in the range [lower, upper]
    :param n: number of points
    :param lower: lower limit
    :param upper: upper limit
    :return: a list of multipressison chebychev points that are in the range [lower, upper]
    """
    #generate chebeshev points on a range [-1, 1]
    index = numpy.arange(1, n+1)
    range_ = abs(upper - lower)
    return [(.5*(mp.cos((2*i-1)/(2*n)*mp.pi)+1))*range_ + lower for i in index]

def poly_generator(coeff, order):
    return lambda x: coeff * (x**order)


func = lambda x: (mp.e)**x
n_degree = 3
lower, upper = -1, 1

y_points = chev_points(n_degree + 2, lower, upper)
x_points = [lower]
x_points.extend(y_points[1:4])
x_points.append(upper)
#print(x_points)

A = mp.matrix(n_degree + 2)
coeffs = numpy.zeros(n_degree + 2)

# place in the E column
mean_error = float('inf')

for i in range(n_degree + 2):
    A[i, n_degree + 1] = (-1) ** (i)
    
vander = numpy.flip(numpy.vander(x_points, n_degree+1), 1)

for i in range(n_degree + 2):
    for j in range(n_degree + 1):
        A[i, j] = vander[i, j]

b = mp.matrix([func(x) for x in x_points])
l = mp.lu_solve(A, b)

coeffs = l[:-1]

minimax_list = [(coeffs[index], index) for index in range(len(coeffs))]
minimax = lambda x: sum(poly_generator(coeff, order)(x) for coeff,order in minimax_list)

residual = lambda x: func(x) - minimax(x)

#interval

#intervals = [lower]
#for i in range(n_degree):
#    intervals.append(scipy.optimize.bisect(residual, intervals[i], ))


#scipy.optimize.bistect()


points = numpy.linspace(-1, 1, 1000)

plt.plot(points, func(points) - minimax(points))
plt.scatter(x_points, [func(pt) - minimax(pt) for pt in x_points])
plt.savefig('remez_example')