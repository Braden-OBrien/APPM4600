# import libraries
import numpy as np
import matplotlib.pyplot as plt
    
def driver():

# test functions 
     f = lambda x: x-4*np.sin(2*x)-3

     space = np.arange(-5, 5, 0.01)
     vals = f(space)
     plt.plot(space, vals)
     plt.plot(space, [0]*len(vals))
     plt.savefig('figure')

     f1 = lambda x: -np.sin(2*x) + 5*x/4 - 3/4

     Nmax = 100
     tol = 1e-11

# test f1 '''
     x0 = -0.8
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point for x =', x0, 'is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

     x0 = -0.5
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point for x =', x0, 'is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

     x0 = 1.7 
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point for x =', x0, 'is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

     x0 = 3.1
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point for x =', x0, 'is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

     x0 = 4.5
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point for x =', x0, 'is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)


# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()
