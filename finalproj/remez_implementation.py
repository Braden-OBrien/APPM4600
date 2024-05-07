import numpy as np
import scipy
import scipy.linalg
import scipy.optimize
import matplotlib.pyplot as plt

def cheby_nodes(n: int, a: float, b: float):
    """Generate a set of n Chebyshev Nodes over interval [a, b]"""
    iter = np.arange(1, n+1)
    return [(np.abs(b-a)/2)*(np.cos((np.pi)*((2*i-1)/(2*n))))+(np.abs(a+b)/2) for i in iter]

def remez_polynomial(f, a, b, degree=5, err_tol=1e-6, max_iter=10, ret_interp_nodes=0, saveplots=0, savelogplots=0):
    """Polynomial implementation of the Remez Algorithm
       Returns -> (polynomial, residual, err_max)"""
    
    err_tol+=1

    def poly_generator(coeff, order):
        """Helper function to quickly form polynomials"""
        return lambda x: coeff * (x**order)

    y_points = cheby_nodes(degree + 2, a, b)
    x_points = [b]
    x_points.extend(y_points[1:degree+1])
    x_points.append(a)

    for loop in range(max_iter):

        A = np.matrix([np.zeros(degree + 2) for i in range(degree+2)])
        coeffs = np.zeros(degree + 2)

        for i in range(degree + 2):
            A[i, degree + 1] = (-1)**i
            
        vander = np.flip(np.vander(x_points, degree+1), 1)
        
        for i in range(degree + 2):
            for j in range(degree + 1):
                A[i, j] = vander[i, j]

        b = np.matrix([f(x) for x in x_points])

        l = scipy.linalg.lu_solve(scipy.linalg.lu_factor(A), b.T)

        coeffs = l[:-1]

        minimax_list = [(coeffs[index], index) for index in range(len(coeffs))]
        minimax = lambda x: sum(poly_generator(coeff, order)(x) for coeff,order in minimax_list)

        residual = lambda x: f(x) - minimax(x)

        extrema_est = x_points[1:degree+1]
        extrema_list = []

        for extrema in extrema_est:
            if (residual(extrema) < 0):
                extrema_list.append(scipy.optimize.fmin(residual, extrema, xtol=1e-9, disp=0)[0])
            else:
                extrema_list.append(scipy.optimize.fmin((lambda x: -1*residual(x)), extrema, xtol=1e-9, disp=0)[0])
        
        errors = [np.abs(x_points[i]-extrema_list[i-1]) for i in range(1, degree+1)]
        
        if(max(errors) <= err_tol * min(errors)):
            break
        
        points = np.linspace(-1, 1, 1000)
        
        if(saveplots):
            plt.clf()
            plt.plot(points, residual(points))
            plt.scatter(x_points, [residual(pt) for pt in x_points])
            plt.savefig('remez_iterative_log'+str(loop))
        if(savelogplots):
            plt.clf()
            plt.plot(points, np.log10(np.abs(residual(points))))
            plt.scatter(x_points, [np.log10(np.abs(residual(pt))) for pt in x_points])
            plt.savefig('remez_iterative_log'+str(loop))
        
        x_points[1:degree+1] = extrema_list
        
    if (ret_interp_nodes):
        return (minimax, residual, max(errors), x_points)
    else:
        return (minimax, residual, max(errors))