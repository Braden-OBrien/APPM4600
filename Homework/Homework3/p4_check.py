# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: -16+6*x+12/x

     f2 = lambda x: (2/3)*x+1/(x**2)

     f3 = lambda x: 12/(1+x)

     Nmax = 100
     tol = 1e-15

# test f1 '''
     x0 = 2.00001
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
#test f2 '''
     x0 = 1.44224
     [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)

#test f2 '''
     x0 = 3.000001
     [xstar,ier] = fixedpt(f3,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f3(xstar):',f2(xstar))
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
