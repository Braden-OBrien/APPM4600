import numpy as np
import scipy
import scipy.linalg
import scipy.optimize
import matplotlib.pyplot as plt

def cheby_nodes(n: int, a: float, b: float):
    """Generate a set of n Chebyshev Nodes over interval [a, b]"""
    scale = abs(b-a)
    #return [0.5*scale*(np.cos((i/(n-1))*(np.pi))) for i in range(n)] #Chebyshev of second kind
    return [0.5*scale*(np.cos((np.pi)*((2*i-1)/(2*n)))) for i in range(1, n+1)] #Chebyshev of first kind

def remez_polynomial(f, a, b, degree=5, err_tol=1e-6, max_iter=10, 
                     ret_interp_nodes=0, saveplots=0, savelogplots=0, saveextremaplots=0):
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
        for i in range(len(extrema_est)-1):
            if (extrema_est[i] <= 1e-6):
                extrema_est[i] += extrema_est[i+1]/(degree**5)
        extrema_list = []

        for extrema in extrema_est:
            if (residual(extrema) < 0):
                #extrema_list.append(scipy.optimize.minimize(residual, extrema, method='Nelder-Mead', tol=1e-9).x[0])
                extrema_list.append(scipy.optimize.fmin(residual, extrema, xtol=1e-9, disp=0)[0])
            else:
                #extrema_list.append(scipy.optimize.minimize((lambda x: -1*residual(x)), extrema, method='Nelder-Mead', tol=1e-9).x[0])
                extrema_list.append(scipy.optimize.fmin((lambda x: -1*residual(x)), extrema, xtol=1e-9, disp=0)[0])
        
        errors = [np.abs(residual(extrema_list[i]))[0] for i in range(degree)]
        
        if(saveplots):
            points = np.linspace(-1, 1, 1000)
            plt.clf()
            plt.plot(points, residual(points))
            plt.scatter(x_points, [residual(pt) for pt in x_points])
            plt.savefig('remez_iterative'+str(loop))
        if(savelogplots):
            points = np.linspace(-1, 1, 1000)
            plt.clf()
            plt.plot(points, np.log10(np.abs(residual(points))))
            plt.scatter(x_points, [np.log10(np.abs(residual(pt))) for pt in x_points])
            plt.savefig('remez_iterative_log'+str(loop))
        if(saveextremaplots):
            points = np.linspace(-1, 1, 1000)
            plt.clf()
            plt.plot(points, residual(points))
            plt.scatter(extrema_list, [residual(pt) for pt in extrema_list], color='r')
            plt.savefig('remez_iterative_extrema'+str(loop))
        
        if(max(errors) <= err_tol * min(errors)):
            break
        
        x_points[1:degree+1] = extrema_list
        
    if (ret_interp_nodes):
        return (minimax, residual, max(errors), x_points)
    else:
        return (minimax, residual, max(errors))