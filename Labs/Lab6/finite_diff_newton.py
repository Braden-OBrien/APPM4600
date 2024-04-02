import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt;


def driver():

    x0 = np.array([1, 0])

    h_diff = 1e-7
    
    Nmax = 100
    tol = 1e-10

    t = time.time()
    [xstar,xlist,ier,its] =  FiniteDiffNewton(x0,h_diff,tol,Nmax);
    elapsed = time.time()-t;
    print(xstar);
    print(its);
    err = np.sum((xlist-xstar)**2,axis=1);
    plt.plot(np.arange(its),np.log10(err[0:its]));
    plt.savefig('figure');


def evalF(x):

    F = np.zeros(2)

    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F

def evalJ(x, h):

    J = np.array([[((4*(x[0]+h[0])**2 + (x[1])**2 - 4) - (4*(x[0]-h[0])**2 + (x[1])**2 - 4))/(2*h[0]),
                   ((4*(x[0])**2 + (x[1]+h[1])**2 - 4) - (4*(x[0])**2 + (x[1]-h[1])**2 - 4))/(2*h[1])],
                   
                   [((x[0]+h[0]) + (x[1]) - np.sin(x[0]+h[0] - x[1]) - (x[0]-h[0]) + (x[1]) - np.sin(x[0]-h[0] - x[1]))/(2*h[0]),
                   ((x[0]) + (x[1]+h[1]) - np.sin(x[0] - x[1]+h[1]) - (x[0]) + (x[1]-h[1]) - np.sin(x[0] - x[1]-h[1]))/(2*h[1])]])
    
    return J


def FiniteDiffNewton(x0,h_diff,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;
    h = 1e-32 + (h_diff * x0)

    for its in range(Nmax):
       J = evalJ(x0, h);
       F = evalF(x0);

       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier = 0
           return[xstar, xlist,ier, its];

       x0 = x1
       h = 1e-32 + (h_diff * x0)

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver();
