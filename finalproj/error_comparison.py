import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import remez_poly as remez #credit to GitHub @DKenefake
import mpmath as mp
import scipy

def chev_points(n:int, lower:float = -1, upper:float = 1):
    """
    Generates a set of chebychev points spaced in the range [lower, upper]
    :param n: number of points
    :param lower: lower limit
    :param upper: upper limit
    :return: a list of multipressison chebychev points that are in the range [lower, upper]
    """
    #generate chebeshev points on a range [-1, 1]
    index = np.arange(1, n+1)
    range_ = abs(upper - lower)
    return [(.5*(mp.cos((2*i-1)/(2*n)*mp.pi)+1))*range_ + lower for i in index]

order = 3

f = lambda x: (np.e)**x

pts = np.linspace(-1, 1, 1000)

coeffs, err = remez.remez(f, order, -1, 1)

def poly_generator(coeff, order):
    return lambda x: coeff * (x**order)

minimax_list = [(coeffs[index], index) for index in range(len(coeffs))]
minimax = lambda x: sum(poly_generator(coeff, order)(x) for coeff,order in minimax_list)

cheb = chev_points(order+1, -1, 1)
lagrange = scipy.interpolate.lagrange(cheb, [f(i) for i in cheb])


plt.plot(pts, f(pts))
plt.plot(pts, minimax(pts))
plt.plot(pts, lagrange(pts))
plt.legend(["e^x", "minimax", "lagrange"])
plt.savefig('remez_comparison_plot')

plt.clf()

resid_minimax = lambda x: np.log10(float(np.abs(f(x) - minimax(x))))
resid_lagrange = lambda x: np.log10(float(np.abs(f(x) - lagrange(x))))

plt.plot(pts, [resid_minimax(i) for i in pts])
plt.plot(pts, [resid_lagrange(i) for i in pts])
plt.legend(["minimax", "lagrange"])
plt.savefig('remez_comparison_logplot')